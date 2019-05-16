'''简述ORM原理'''
'''
对用户来说：orm框架目的就是不让用户写sql语句
对框架来说: orm框架就是把类和类的对象转换成sql语句

'''
class User():
    def __int__(self):
        self.id = '01'
        self.name = 'xx'
    def order_by(self):
        sss

obj = User()
obj.__dict__ = {
    id:'',
    name:''
}
#select id,name from user order by sss
#调用第三方的链接数据库的模块（pymysql）

# code first   db first


'''
数据库操作
        ---python
                pymysql:自己拼接sql语句
                sqlalchemy：用类和类的对象以及类中的方法（orm框架）通过pymysql发送sql进行数据库操作
                            可以链接各种数据库,链接数据库的时候会区分数据库的种类
        ---终端
'''
'''
1.安装数据库
2.创建用户 + 授权
3.链接
      --数据库
         终端创建数据库(字符编码)
      --数据表
         终端
         ORM
         Pymysql
             create....)engine=innodb    这个引擎支持事务
      --数据行
          增
          删
          改
          查
            --limit   分页的时候如果数据量大会越来越慢
              分页主要是找区间内的数据，找最后几条的时候会扫描一遍全表，
              加索引的话，会去索引表里扫描一遍
              把每一页的id最大值拿出来，去找下一页的时候从id最大值开始查
            --group by
            --...
                在sqlalchemy里面都有对应的sql操作
                sqlalchemy本身不能操作数据库,通过第三方的模块去操作数据库（pymysql）
                它会把类以及类的对象转换成sql，然后再交给pymysql去操作数据库
                
            
'''
