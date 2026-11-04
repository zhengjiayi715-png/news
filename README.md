# 新闻资讯平台 

一个基于前后端分离架构的全栈新闻资讯应用。
- **小白跟着视频做的第一个项目,轻喷**

## 功能特性

- **移动端优先**：基于 Vant UI 构建，完美适配手机端屏幕。
- **新闻模块**：支持多分类切换、下拉刷新、上拉加载、新闻详情及相关推荐。
- **用户系统**：支持注册、登录、JWT 鉴权、个人资料修改与密码重置。
- **收藏与历史**：支持新闻收藏、浏览历史记录（基于 Redis 缓存与 MySQL 持久化）。
- **AI 智能问答**：集成阿里云百炼

## 技术栈

### 前端 
- **核心框架**：Vue 3 + Vite

### 后端 
- **核心框架**：FastAPI
- **数据库 ORM**：SQLAlchemy 2.0 (Async)
- **数据库**：MySQL (aiomysql)
- **缓存**：Redis (redis.asyncio)

## 项目目录结构

```text
news-app/
├── frontend/                
│   ├── src/                 
│   │   ├── api/             
│   │   ├── components/      
│   │   ├── config/          
│   │   ├── router/          
│   │   ├── store/           
│   │   ├── views/           
│   │   └── main.js               
│   ├── package.json
│   └── vite.config.js
│
├── backend/                 
│   ├── cache/               
│   ├── config/              
│   ├── crud/                
│   ├── models/              
│   ├── routers/             
│   ├── schemas/             
│   ├── utils/               
│   ├── main.py              
│   └── requirements.txt     
│
├── .gitignore               
└── README.md                
```

## 环境要求
- Windows 11
- Python 3.12
- Node.js >= 18.0
- MySQL >= 8.0
- Redis >= 6.0

## 快速开始

```cmd
#1.装前端环境，启动前端
cd frontend
npm install
npm run dev
#2.装后端环境，启动后端
cd backend
.venv\Scripts\activate
pip install -r requirements.txt
#3.3. 初始化数据库：
请先在你的 MySQL 中创建数据库 news_app，然后导入项目根目录 backend/init_db.sql 文件。
```

## 环境变量配置
- 后端中DB_PASSWORD=your_mysql_password
- 因为 AI 对话直接在前端发起请求，你需要配置阿里云百炼的 API Key

## 致谢
- 感谢 **B站/黑马程序员** 的《fastapi实战教程》，本项目的部分前端 UI 灵感与后端业务逻辑参考了该课程。
- 感谢 **[@2205094557](https://github.com/2205094557)** ,你的wallpaper项目激励着我。
- 感谢 **B站/李勃老师**,讲清了许多概念。