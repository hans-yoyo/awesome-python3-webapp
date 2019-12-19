# awesome-python3-webapp

**廖雪峰老师python教程实战环节: 实现一个简易的博客网站**

python版本: 3.7.4

## 搭建开发环境

下载第三方库

```shell
# 异步框架
pip install aiohttp
# 前端模板引擎
pip install jinja
# MySQL异步驱动程序
pip install aiomysql
```
目录结构

```
|__backup 备份
|__conf   配置文件
|__dist   打包目录
|__www    Web目录
    |__static  静态资源
    |__templates  模版文件
```
## 编写项目骨架

## 编写ORM

## 编写Model

## 编写Web框架

## 编写配置文件

## 编写MVC

## 构建前端

- UIkit前端组件
- HTML模版复用

## 编写API

## 完成用户登录和注册

用户口令：
```plain
"用户id" + "过期时间" + SHA1("用户id" + "用户口令" + "过期时间" + "SecretKey")
```

app.py中auth_factory用来做登录校验，并将user放入request域

## 编写日志创建页

## 编写日志列表页

## 配置热部署

Python第三方库watchdog监控目录文件的变化
```shell
pip install watchdog
```

## 完成、部署项目

后端API包括：

- 获取日志：GET /api/blogs

- 创建日志：POST /api/blogs

- 修改日志：POST /api/blogs/:blog_id

- 删除日志：POST /api/blogs/:blog_id/delete

- 获取评论：GET /api/comments

- 创建评论：POST /api/blogs/:blog_id/comments

- 删除评论：POST /api/comments/:comment_id/delete

创建新用户：POST /api/users

- 获取用户：GET /api/users

- 管理页面包括：

- 评论列表页：GET /manage/comments

- 日志列表页：GET /manage/blogs

- 创建日志页：GET /manage/blogs/create

- 修改日志页：GET /manage/blogs/

- 用户列表页：GET /manage/users

用户浏览页面包括：

- 注册页：GET /register

- 登录页：GET /signin

- 注销页：GET /signout

- 首页：GET /

- 日志详情页：GET /blog/:blog_id


