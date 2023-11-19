---
layout: post
cid: 446
title: Jupyter Notebook设置密码
slug: 446
date: 2021/12/12 18:06:27
updated: 2023/11/14 15:51:40
status: publish
author: admin
categories: 
  - 默认分类
tags: 
  - docker
---


一、生成配置文件<br />
进入cmd控制台，输入如下命令：<br />
<br />
jupyter notebook --generate-config<br />
<br />
执行以上命令后会在用户目录下会产生一个.jupyter文件夹，如下图所示：<br />
<br />
文件夹中会有一个jupyter_notebook_config.py文件。<br />
<br />
二、生成密码<br />
打开Jupyter Notebook,执行以下代码(如果没有办法打开自己的jupyter，可在其他可执行以下代码的地方去执行，此步骤的目的只是执行python代码去生成一个密文)：<br />
<br />
from notebook.auth import passwd<br />
p = passwd()<br />
print(p)<br />
这个时候就会让你设置密码。<br />
连续输入两次密码后，你会得一个字符串（sha1:…），也就是加密后的密码，如图所示：<br />
<br />
把得到的这个字符串复制下来。<br />
<br />
三、把密码写入配置文件<br />
打开第一步产生的jupyter_notebook_config.py文件。<br />
找到下图所示的那一行：<br />
#c.NotebookApp.password = ''<br />
把前面的注释删掉，再把第二步复制的字符串粘贴过来：<br />
<br />
保存，完成。<br />
<br />
重启Jupyter Notebook,会要求你输入密码：<br />
<br />
输入你之前设置的密码就可以了。<br />
————————————————<br />
版权声明：本文为CSDN博主「大屁孩。」的原创文章<br />
原文链接：<a href="https://blog.csdn.net/smile_Shujie/article/details/88357371" target="_blank">https://blog.csdn.net/smile_Shujie/article/details/88357371</a><br />