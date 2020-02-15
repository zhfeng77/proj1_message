- 1.完成django留言簿项目目录结构的构建
- 2.配置静态目录：应用中的静态目录和全局静态目录，删除测试用的app2应用
- 3.方式1：将message_form.html中的样式分离出来，保存到apps/message_form/static/css目录中命名为style.css
在message_form.html中添加对样式的引用<link rel="stylesheet" href="/static/css/style.css">
方式2:将样式文件放在项目根目录下的static/css目录中，在settings.py中添加STATICFILES_DIRS完成对static路径的设置
- 4.建立与页面相关的数据库，并修改数据引擎为mysql，安装mysql的django驱动mysqlclient
建立和message表和与页面数据相对应的字段
- 5.从数据库中获取数据并展示（views.py)
通过all,filter,get来获取数据，通过delete删除数据，通过save插入或更新数据
- 6 从前端页面(html)提取数据存入数据库
将message_form.html中<form action="/form/，改为<form action="/message_form/与urls.py中的    
path('message_form/', message_form)相对应，表示点击提交(submit)按钮时会显示message_form/页面
如果直接提交页面，会产生403错误，需要在</form>前添加 {% csrf_token %}
通过request.POST.get()获取页面中的数据
通过数据对象message = Message()的save()将数据写入数据库中
-7 从数据库中读取数据在前端页面中显示
采用同一个处理函数message_form来处理 页面数据提取和读取数据在页面显示，一个是POST，一个是GET，通过request.method来判断
if request.method=="POST"
获取数据库中的数据：
if request.method == "GET":
    all_messages = Message.objects.all()
    if all_messages:
        message = all_messages[0]   取第1个数据
            return render(request,"message_form.html", {
                "message": message     #返回key:value形式的数据， 在message_form.html中可以用Django提供的模板语言引用这些数据
            })