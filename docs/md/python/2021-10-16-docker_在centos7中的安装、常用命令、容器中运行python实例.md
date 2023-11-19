---
layout: post
cid: 440
title: docker 在centos7中的安装、常用命令、容器中运行python实例
slug: 440
date: 2021/10/16 21:58:24
updated: 2023/11/14 15:51:40
status: publish
author: admin
categories: 
  - python
tags: 
---


docker 在centos7中的安装、常用命令、容器中运行python实例<br />
一、CentOS7 中安装 docker<br />
二、基本命令<br />
三、容器操作命令<br />
四、镜像操作命令<br />
五、实例（安装python3.9.0a4）<br />
一、CentOS7 中安装 docker<br />
# 安装 docker 的yum源<br />
yum-config-manager --add-repo https://mirrors.ustc.edu.cn/docker-ce/linux/centos/docker-ce.repo<br />
# 更新源缓存<br />
yum makecache fast&nbsp;&nbsp;<br />
<br />
# 安装 docker 依赖包<br />
yum install -y yum-utils device-mapper-persistent-data lvm2<br />
<br />
# 添加 docker 用户和组<br />
groupadd docker<br />
useradd -g docker docker<br />
<br />
# 安装&nbsp; docker<br />
yum -y install docker<br />
<br />
# systemctl 管理<br />
systemctl start docker<br />
systemctl enable docker<br />
<br />
# 查看 docker 版本<br />
docker version<br />
<br />
# （可以不需要，只是测试）运行 hello world<br />
docker run hello-world<br />
<br />
二、基本命令<br />
# 查看 docker 版本<br />
docker version<br />
<br />
# 查看镜像、容器、数据卷所占用的空间<br />
docker system df<br />
<br />
三、容器操作命令<br />
# 登录<br />
docker login<br />
<br />
# 查看运行中的容器<br />
docker ps<br />
# 查看所有容器<br />
docker ps -a<br />
# 查看所有容器id<br />
docker ps -a -q<br />
<br />
# 删除容器<br />
docker rm [容器id 或者 容器名称]<br />
<br />
# 删除所有容器<br />
docker rm $(docker ps -a -q)<br />
<br />
# 启动容器<br />
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]<br />
docker run --name mysql-docker -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql:5.7.23<br />
# --name 容器运行后的名字<br />
# -d 后台运行<br />
# -p 做端口映射，不然外部不能访问<br />
# -e MYSQL_ROOT_PASSWORD mysql特有的，对应root密码<br />
<br />
# 停止容器<br />
docker stop [容器id]<br />
<br />
# 停止所有容器<br />
docker stop $(docker ps -a -q)<br />
<br />
# 启动容器<br />
docker start [OPTIONS] CONTAINER [CONTAINER...]<br />
<br />
# 重启容器<br />
docker restart [OPTIONS] CONTAINER [CONTAINER...]<br />
<br />
# 进入容器<br />
docker exec -it [CONTAINER ID] /bin/bash<br />
<br />
# 打包容器<br />
docker commit -a "[作者]" -m "[说明]" [容器id] [镜像名称]:[TAG]<br />
<br />
四、镜像操作命令<br />
# 查看镜像<br />
docker images<br />
<br />
# 删除镜像<br />
docker rmi [镜像id 或者 仓库名称:版本号]<br />
<br />
# 打标签<br />
docker tag [镜像id] registry.cn-hangzhou.aliyuncs.com/hxiao/[镜像]:[版本号]<br />
<br />
# 下载镜像<br />
docker pull [OPTIONS] NAME[:TAG|@DIGEST]<br />
docker pull registry.cn-hangzhou.aliyuncs.com/hxiao/[镜像]:[版本号]<br />
<br />
# 上传镜像<br />
docker push [OPTIONS] NAME[:TAG]<br />
docker push registry.cn-hangzhou.aliyuncs.com/hxiao/[镜像]:[版本号]<br />
<br />
# 搜索镜像<br />
docker search [镜像名]<br />
<br />
# 保存镜像<br />
# 基于已有的 docker 容器，做一个新的 docker image<br />
docker commit &lt;container_id&gt; &lt;image_name&gt;<br />
docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]<br />
# -a 作者信息<br />
# -m 提交消息<br />
# -p 提交时暂停容器运行<br />
<br />
# 查看镜像信息<br />
docker inspect &lt;image_id&gt;<br />
<br />
# 导出镜像并保存<br />
docker save [OPTIONS] IMAGE [IMAGE...]<br />
docker save -o ubuntu.tar docker.io/ubuntu<br />
# -o, --output<br />
<br />
# 载入镜像<br />
docker load [OPTIONS]<br />
docker load -i ubuntu.tar<br />
docker load &lt; ubuntu.tar<br />
# -i, --input<br />
# -q, --quiet<br />
五、实例（安装python3.9.0a4）<br />
# 在 https://hub.docker.com/_/python?tab=tags 查询可以下载的版本<br />
# 下载python<br />
docker pull python:3.9.0a4<br />
# --name指定容器名运行容器；<br />
# -i：交互式操作；<br />
# -t：终端；这里打算进入 bash 执行一些命令，并查看返回结果，因此需要交互式终端；<br />
# -d：后台运行；<br />
docker run -itd --name python-test python:3.9.0a4<br />
# 进入容器内，可执行安装好的镜像的命令<br />
docker exec -it python-test bash<br />
# 不进入容器执行命令<br />
docker exec -it python-test pip show ipython<br />
原文链接：https://blog.csdn.net/qq_36072270/article/details/104717968<br />