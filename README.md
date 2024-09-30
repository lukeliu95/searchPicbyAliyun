# 特殊订单图像搜索

这是一个基于Flask的Web应用程序，允许用户上传图片并进行图像搜索。该项目使用阿里云的图像搜索服务来实现图像搜索功能。

## 安装

1. 克隆此仓库到本地：

    ```bash
    git clone https://github.com/lukeliu95/searchPicbyAliyun.git
    cd your-repo-name
    ```

2. 创建并激活虚拟环境：

    ```bash
    python -m venv venv
    source venv/bin/activate  # 对于Windows用户，使用 `venv\Scripts\activate`
    ```

## 使用

1. 启动Flask应用：

    ```bash
    python app.py
    ```

2. 打开浏览器并访问 `http://127.0.0.1:5000`。

## 文件结构

- `app.py`：Flask应用的主文件，定义了路由和处理逻辑。
- `searchPic.py`：包含与阿里云图像搜索服务交互的逻辑。
- `templates/index.html`：前端页面模板，用户可以在此页面上传图片并查看搜索结果。
- `key.py`：存储阿里云的AccessKey ID和AccessKey Secret（请勿将此文件上传到公共仓库）。

## 配置

在 `key.py` 文件中，添加您的阿里云AccessKey ID和AccessKey Secret：

## 功能

- 用户可以上传图片。
- 应用将图片发送到阿里云图像搜索服务进行搜索。
- 搜索结果以图片形式展示，用户可以点击图片查看大图。