#do_orm.py
'''  原文：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000
ORM全称“Object Relational Mapping”，即对象-关系映射，
就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，
这样，写代码更简单，不用直接操作SQL语句。
'''
class Filed(object):

    def __init__(self,name,column_type):
        self.name = name 
        self.columu_type = column_type
    
    def __str__(self):
        return '{}:{}'.format(self.__class__.__name__,self.name)
        
class StringField(Filed):

    def __init__(self, name):
        super(StringField,self).__init__(name, 'varchar(100)')
    

class IntegerField(Filed):

    def __init__(self, name):
        super(IntegerField,self).__init__(name, 'bigint')

'''ModelMetaclass:
1.排除掉对Model类的修改；
2.在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，
就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，
否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
3.把表名保存到__table__中，这里简化为表名默认为类名。
'''
class ModelMetaclass(type):

    def __new__(cls,name,bases,attrs):
        if name =='Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model: {}'.format(name))
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,Filed):
                print('Found mapping: {}==>{}'.format(k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  #保存属性和列的关系映射
        attrs['__table__'] = name         #假设表名和类名一致
        return type.__new__(cls,name,bases,attrs)

'''
在Model类中，定义各种操作数据库的方法
'''
class Model(dict,metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model,self).__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '{}'".format(key))

    def __setattr__(self, Key, value):
        self[Key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql = 'insert into {} ({}) values ({})'.format(self.__table__,','.join(fields),','.join(params))
        print('SQL: {}'.format(sql))
        print('ARGS: {}'.format(str(args)))
'''
当用户定义一个class User(Model)时，Python解释器首先在当前类
User的定义中查找metaclass，如果没有找到，就继续在父类Model中
查找metaclass，找到了，就使用Model中定义的metaclass的ModelMetaclass
来创建User类，也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。
'''
class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()
