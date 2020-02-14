from django.shortcuts import render

# 导入models.py中定义的模型Message类
from apps.message_form.models import Message


def message_form(request):
    # 从models中获取数据
    all_messages = Message.objects.all()    # 获取所有数据
    # 切片操作
    # all_messages = Message.objects.all()[:1]  获取第1个数据
    # 遍历
    # for message in all_messages:
    #     print(message.name, message.email, message.address, message.message)
    #     print(all_messages.query)


    # filter
    # all_messages = Message.objects.filter(name='zhf')
    # all_messages = Message.objects.filter(email='z@z.z')
    # for message in all_messages:
    #     print(message.name)
    #     print(all_messages.query)

    # get
    # message = Message.objects.get(name='zhf')
    # 找到多个结果时会抛异常
    # 偷懒的异常捕获写法，不推荐
    # try:
    #     message = Message.objects.get(email='z@z.z')
    #     print(message.email)
    # except Exception as e:
    #     print(e)

    # try:
    #     message = Message.objects.get(email='z@z.z')
    #     print(message.email)
    # except Message.MultipleObjectsReturned as e:
    #     print(e,'发生异常，get返回了多条数据')
    # except Message.DoesNotExist as e:
    #     print(e,'发生异常，查找的数据不存在')

    # delete方法
    # all_messages = Message.objects.filter(name='zhf')
    # all_messages.delete()   # 将用filter中满足条件的数据全部删除

    # save方法，不存在时是创建数据，存在时是更新数据
    # message = Message()
    # message.name='test'
    # message.address="测试地址"
    # message.email="测试邮件地址abc"
    # message.message="测试的消息内容"
    # message.save()


    # 点击了提交按钮
    if request.method =="POST":    # 点击submit按钮时会是一个post请求  <input type="submit" class="button" value="提交"/>
        # 获取页面提交的数据
        name = request.POST.get('name')  #<input id="name" type="text" name="name" class="error" placeholder="请输入您的姓名"/>
        email = request.POST.get('email')#  <input id="email" type="email" value="" name="email" placeholder="请输入邮箱地址"/>
        address =request.POST.get('address')
        message_text = request.POST.get('message')
        print(name,email,address,message_text)

        # 将数据写入数据库
        #创建数据对象
        message = Message()     #创建模型对象(model_instance)
        message.name = name
        message.email=email
        message.address = address
        message.message = message_text
        #将数据写入数据库
        message.save()
        print('成功保存一条记录')


    return render(request, "message_form.html")