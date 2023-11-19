---
layout: post
cid: 445
title: 在服务器上使用docker安装Jupyter Notebook
slug: 445
date: 2021/12/12 16:59:56
updated: 2023/11/14 15:51:40
status: publish
author: admin
categories: 
  - 学习记录
tags: 
  - docker
---


一：前言<br />
使用docker快速安装Jupyter Notebook，来在远程快速编写python代码并运行<br />
<br />
二：步骤<br />
本文仅简略描述安装过程，对于安装那个版本请看官网，本文采用jupyter/datascience-notebook:9b06df75e445<br />
<br />
docker run --rm -p 8003:8888 --name 'jupyter_notebook' -dit -e JUPYTER_ENABLE_LAB=yes -v "$PWD":/home/jovyan/work jupyter/datascience-notebook:9b06df75e445<br />
本代码指定8003的服务器端口连接容器的8888端口，并取名'jupyter_notebook'<br />
<br />
同时使用-dit 来让docker容器在后端运行。-v 挂载本机的/home/www 至容器的/home/jovyan/work ，因此存储在此文件夹的文件在容器消失后仍在本机中。<br />
<br />
在浏览器中输入 IP:8003 进行访问，会出现如下页面。<br />
<br />
<br />
它要求token，可是他在后端运行，该怎么办呢.<br />
<br />
于是 使用 docker ps命令来查看该容器的id 并获取<br />
<br />
再用 docker logs id 来获取这个容器的后台日志，如此就可以获得token，并在页面中输入并设置密码了。<br />
<br />
之后就可以看见页面了<br />
<br />
原文链接：<a href="https://blog.csdn.net/jomes_wang/article/details/111628259" target="_blank">https://blog.csdn.net/jomes_wang/article/details/111628259</a><br />