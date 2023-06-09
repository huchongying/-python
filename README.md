
django+layui+swiper
# 项目名称：南航学校官网

## 项目介绍
南航学校官网是基于Django框架、Layui前端框架以及Swiper轮播插件开发的一个网站。它旨在为南航学校的师生、校友和访客提供一个信息丰富、易于访问和使用的在线平台，以展示学校的学术、科研、活动和其他相关信息。

## 项目特点
- 基于Django框架：使用Django框架能够快速构建稳定、高效的Web应用程序，并提供丰富的功能和强大的安全性。
- 使用Layui前端框架：Layui是一个简单易用、灵活且功能强大的前端框架，它提供了丰富的UI组件和交互效果，使得网站界面设计更加美观和用户友好。
- 集成Swiper轮播插件：Swiper是一个流行的轮播插件，通过它可以实现图片、文字等内容的轮播展示，为网站增添了动态和吸引力。

## 主要功能
1. 首页展示：通过Swiper插件实现首页的轮播图片展示，突出学校的特色和重要信息。
2. 导航菜单：提供清晰的导航菜单，方便用户浏览和访问不同的页面。
3. 学校简介：展示学校的基本信息、历史沿革、校园风光等，让用户了解学校的背景和特点。
4. 学院与专业：介绍学校的各个学院和专业设置，帮助用户了解学校的学科结构和专业方向。
5. 教师与科研：展示学校的优秀教师和科研成果，以及相关的学术活动和项目信息。
6. 招生与就业：提供学校的招生政策、录取信息和就业指导，帮助学生和家长获取招生和就业相关的信息。
7. 校园生活：介绍学校的校园生活和文化活动，包括学生组织、社团活动、体育赛事等。
8. 校友会：展示校友会的组织结构、活动动态和校友资源，促进校友之间的联系和交流。

## 部署说明
1. 确保服务器环境中已安装Python和Django框架。
2. 克隆项目代码到服务器本地目录。
```
git clone https://github.com/huchongying/-python.git
```
3. 在项目根目录中创建虚拟环境，可以使用以下命令：
python3 -m venv venv

4. 激活虚拟环境：
- Windows：
  ```
  venv\Scripts\activate
  ```
- macOS/Linux：
  ```
  source venv/bin/activate
  ```
5. 安装项目依赖：
```pip install -r requirements.txt```
```pip install django```
```pip install mysqlclient```
6. 运行数据库迁移：
```python manage.py migrate```
7.对数据库内容进行修改，在根目录的settings.py文件下的：
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'root',
        'PASSWORD': '20020221',
        'HOST': '127.0.0.1',
        'PORT': 3306,
    }
}
```
对数据库名和数据库账户进行相应的修改

8.终端中输入···py manage.py runserver···
