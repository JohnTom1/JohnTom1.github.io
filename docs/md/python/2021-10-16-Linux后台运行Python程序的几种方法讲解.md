---
layout: post
cid: 438
title: Linux后台运行Python程序的几种方法讲解
slug: 438
date: 2021/10/16 21:53:39
updated: 2023/11/14 15:51:40
status: publish
author: admin
categories: 
  - python
tags: 
---


<h1 class="title" style="margin:0px;padding:0px 5px 5px;outline:none;font-size:20px;color:#333333;line-height:35px;overflow:hidden;font-family:微软雅黑;white-space:normal;">
	<span style="font-family:tahoma, arial, &quot;font-size:16px;white-space:normal;background-color:#FFFFFF;">1.第一种方法是直接用unhup命令来让程序在后台运行，命令格式如下：</span>
</h1>
<h1 class="title" style="margin:0px;padding:0px 5px 5px;outline:none;font-size:20px;color:#333333;line-height:35px;overflow:hidden;font-family:微软雅黑;white-space:normal;">
	unhup python 文件名.py (&gt; ***.log )&amp;
</h1>
<h1 class="title" style="margin:0px;padding:0px 5px 5px;outline:none;font-size:20px;color:#333333;line-height:35px;overflow:hidden;font-family:微软雅黑;white-space:normal;">
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;font-family:tahoma, arial, &quot;font-size:16px;white-space:normal;background-color:#FFFFFF;">
		在这个命令中，python指定我们要执行的文件为python文件，后面的文件名.py即是我们要执行的文件。括号内容表示可以将平时输出到控制台中的内容重定向到*.log这个文件中，这个是可选的，如果没有这个，则会默认输出到nohup.out文件中。括号后面你的&amp;表示后台运行。
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;font-family:tahoma, arial, &quot;font-size:16px;white-space:normal;background-color:#FFFFFF;">
		2.第二种方法是写一个脚本，然后把脚本提交给服务器，让服务器在后台运行脚本里面的语句。假设我们定义了一个脚本start.sh，其内容如下：
	</p>
#!/bin/bash<br />
cd 想要运行文件的路径名<br />
python -u ***.py<br />
<span style="font-family:tahoma, arial, &quot;font-size:16px;white-space:normal;background-color:#FFFFFF;">上述脚本中，#!/bin/bash是指此脚本使用/bin/bash来解释执行下面的语句，其中cd是表示将当前目录跳到所要运行文件所在目录，然后python -u ***.py则表示运行***python文件，当写完该脚本后，我们就可以使用下面的这条命令来执行该脚本从而让程序在后台运行：</span>
</h1>
<h1 class="title" style="margin:0px;padding:0px 5px 5px;outline:none;font-size:20px;color:#333333;line-height:35px;overflow:hidden;font-family:微软雅黑;white-space:normal;">
	./start.sh &gt; result.log &amp;<br />
</h1>
<div>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;font-family:tahoma, arial, &quot;font-size:16px;white-space:normal;background-color:#FFFFFF;">
		在这里./start.sh表示运行当前目录下的脚本start.sh，&gt; result.log表示把原来输出到控制台的东西都输出到result.log文件中，&amp;表示在后台运行
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;font-family:tahoma, arial, &quot;font-size:16px;white-space:normal;background-color:#FFFFFF;">
		我们通过ps -e命令可以查看后台运行的进程都有哪些
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;font-family:tahoma, arial, &quot;font-size:16px;white-space:normal;background-color:#FFFFFF;text-align:center;">
		<img id="theimg" src="https://img.jbzj.com/file_images/article/201902/2019226105319881.png?2019126105332" alt="" style="border-width:1px;border-style:solid;border-color:#CCCCCC;vertical-align:middle;padding:1px;overflow:hidden;max-width:816px;" />
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;font-family:tahoma, arial, &quot;font-size:16px;white-space:normal;background-color:#FFFFFF;">
		上图我们可以看到，我们的脚本start.sh和Python程序都已经在后台成功运行，然后通过cat result.log | more就可以来查看原来输出到控制台的信息
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;font-family:tahoma, arial, &quot;font-size:16px;white-space:normal;background-color:#FFFFFF;">
		注：要想执行python文件中的某个函数，一定要记得除了要定义该函数外，还要在该文件中调用该函数
	</p>
转载自<a href="https://www.jb51.net/article/156969.htm" target="_blank">https://www.jb51.net/article/156969.htm</a><br />
</div>