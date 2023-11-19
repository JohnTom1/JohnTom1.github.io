---
layout: post
cid: 439
title: CentOS 7如何实现定时执行python脚本
slug: 439
date: 2021/10/16 21:55:34
updated: 2023/11/14 15:51:40
status: publish
author: admin
categories: 
  - python
tags: 
---


<h1 class="title" style="margin:0px;padding:0px 5px 5px;outline:none;font-size:20px;color:#333333;line-height:35px;overflow:hidden;font-family:微软雅黑;white-space:normal;">
	<br />
</h1>
<div class="lbd clearfix" style="margin:0px auto;padding:0px;outline:none;width:820px;text-align:center;color:#222222;font-family:tahoma, arial, &quot;font-size:14px;white-space:normal;">
</div>
<div class="summary" style="margin:10px 0px;padding:10px;outline:none;background:#EBF5FD;color:#333333;border-left:3px solid #49A7EA;font-size:16px;line-height:26px;font-family:tahoma, arial, &quot;white-space:normal;">
	这篇文章主要介绍了CentOS 7如何实现定时执行python脚本,文中通过示例代码介绍的非常详细，对大家的学习或者工作具有一定的参考学习价值,需要的朋友可以参考下
</div>
<div class="lbd clearfix" style="margin:0px auto;padding:0px;outline:none;width:820px;text-align:center;color:#222222;font-family:tahoma, arial, &quot;font-size:14px;white-space:normal;">
	<ins class="adsbygoogle" data-ad-client="ca-pub-6384567588307613" data-ad-slot="3921475131" data-ad-format="auto" style="text-decoration-line:none;display:block;">
	</ins>
</div>
<div id="content" style="margin:0px auto;padding:0px;outline:none;line-height:32px;clear:both;font-size:16px;word-break:break-all;overflow:hidden;color:#222222;font-family:tahoma, arial, &quot;white-space:normal;">
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		在CentOS下，可以使用crontab进行定时任务的处理。
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		<strong>一、crontab的安装</strong>
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		默认情况下，CentOS 7中已经安装有crontab，如果没有安装，可以通过yum进行安装。
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		<code style="margin:0px 0.3em;padding:0.2em 0.6em;outline:none;font-style:inherit;font-weight:inherit;background:#EBF5FD;width:640px;line-height:1.5;clear:both;font-size:14px;border:1px solid #DDDDDD;color:#333333;border-radius:3px;font-family:Menlo, Monaco, Consolas, &quot;">yum install crontabs</code>
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		<strong>二、crontab的定时语法说明</strong>
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		corntab中，一行代码就是一个定时任务，其语法结构可以通过这个图来理解。
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;text-align:center;">
		<img loading="lazy" alt="" src="https://img.jbzj.com/file_images/article/202006/202006240958236.png" style="border-width:1px;border-style:solid;border-color:#CCCCCC;vertical-align:middle;padding:1px;overflow:hidden;max-width:816px;" />
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		字符含义如下：
	</p>
	<blockquote style="margin:0px auto 10px;padding:4px 4px 4px 10px;outline:none;background:#F1F7FD;border-left:3px solid #9ECEF1;">
		<p style="margin-top:0px;margin-bottom:0px;padding:0px 4px;outline:none;line-height:30px;">
			* 代表取值范围内的数字<br />
/ 代表"每"<br />
- 代表从某个数字到某个数字<br />
, 代表离散的取值(取值的列表)
		</p>
	</blockquote>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		一些常用的时间写法如下：
	</p>
	<blockquote style="margin:0px auto 10px;padding:4px 4px 4px 10px;outline:none;background:#F1F7FD;border-left:3px solid #9ECEF1;">
		<p style="margin-top:0px;margin-bottom:0px;padding:0px 4px;outline:none;line-height:30px;">
			* * * * * //每分钟执行<br />
* */4 * * * //每4小时执行<br />
0 4 * * * //每天4点执行<br />
0 12 */2 * * //每2天执行一次，在12点0分开始运行<br />
* * * * 0 //每周日执行<br />
* * * * 6,0 //每周六、日执行<br />
5 * * * * //每小时的第5分钟执行
		</p>
	</blockquote>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		<strong>三、配置定时执行python脚本</strong>
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		由于是需要定时执行python脚本，所以应该使用如下命令：
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		<code style="margin:0px 0.3em;padding:0.2em 0.6em;outline:none;font-style:inherit;font-weight:inherit;background:#EBF5FD;width:640px;line-height:1.5;clear:both;font-size:14px;border:1px solid #DDDDDD;color:#333333;border-radius:3px;font-family:Menlo, Monaco, Consolas, &quot;">python xxx.py</code>
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		但是非常重要的一点是要用绝对路径写到命令，否则定时运行失败。因此我们需要先弄清楚python的具体路径。
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		我们在服务器上有python2和python3两个版本，通过如下命令来查看其安装路径。
	</p>
	<blockquote style="margin:0px auto 10px;padding:4px 4px 4px 10px;outline:none;background:#F1F7FD;border-left:3px solid #9ECEF1;">
		<p style="margin-top:0px;margin-bottom:0px;padding:0px 4px;outline:none;line-height:30px;">
			# which python //查看系统默认安装的python2的路径<br />
/usr/bin/python<br />
# which python3 //查看自行安装的python3的路径<br />
/usr/bin/python3
		</p>
	</blockquote>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		用如下命令查看当前系统中的定时任务列表
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		<code style="margin:0px 0.3em;padding:0.2em 0.6em;outline:none;font-style:inherit;font-weight:inherit;background:#EBF5FD;width:640px;line-height:1.5;clear:both;font-size:14px;border:1px solid #DDDDDD;color:#333333;border-radius:3px;font-family:Menlo, Monaco, Consolas, &quot;"># crontab -l</code> 
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		对crontab进行编辑
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		<code style="margin:0px 0.3em;padding:0.2em 0.6em;outline:none;font-style:inherit;font-weight:inherit;background:#EBF5FD;width:640px;line-height:1.5;clear:both;font-size:14px;border:1px solid #DDDDDD;color:#333333;border-radius:3px;font-family:Menlo, Monaco, Consolas, &quot;"># crontab -e</code> 
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		在其中增加如下的内容（每小时的00分执行一个获取微信accesstoken的py脚本），注意python的版本用到了3
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		<code style="margin:0px 0.3em;padding:0.2em 0.6em;outline:none;font-style:inherit;font-weight:inherit;background:#EBF5FD;width:640px;line-height:1.5;clear:both;font-size:14px;border:1px solid #DDDDDD;color:#333333;border-radius:3px;font-family:Menlo, Monaco, Consolas, &quot;">00 * * * * /usr/bin/python3 /usr/local/wechatapi/wechat_accesstoken.py</code>
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		完成后，可以重启一下crontab的服务即可。
	</p>
	<p style="margin-top:0px;margin-bottom:0px;padding:3px 0px;outline:none;line-height:30px;">
		<code style="margin:0px 0.3em;padding:0.2em 0.6em;outline:none;font-style:inherit;font-weight:inherit;background:#EBF5FD;width:640px;line-height:1.5;clear:both;font-size:14px;border:1px solid #DDDDDD;color:#333333;border-radius:3px;font-family:Menlo, Monaco, Consolas, &quot;">service crond restart<br />
转载自https://www.jb51.net/article/189415.htm</code>
	</p>
</div>