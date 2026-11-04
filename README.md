# 新闻资讯平台 

一个基于前后端分离架构的全栈新闻资讯应用。

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