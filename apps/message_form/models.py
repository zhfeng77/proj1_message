from django.db import models


class Message(models.Model):
    # 这里的verbose_name用于给字段一个可读性好的名字，如果不指定，则使用变量名，比如name
    # prmary_key表示该字段是一个主键，如果不指定，会自动帮你生成一个id作为主键
    name = models.CharField(max_length=20, verbose_name="姓名", primary_key=True)
    email = models.EmailField(verbose_name="邮箱")
    address = models.CharField(max_length=200, verbose_name="联系地址")
    message = models.TextField(verbose_name="留言")

    class Meta():   #Meta选项用于定义一些Django模型类的行为特性
        verbose_name = "留言信息"           # verbose_name用于给你的模型类起一个可读性好的名字
        verbose_name_plural = verbose_name # 这个选项是指定，模型的复数形式是什么，如果不指定Django会自动在模型名称后加一个’s’
        db_table = "message"                # 定义数据库中的表名