---
layout: post
cid: 374
title: 如何通过gzip和nginx来提高网站打开速度及整体性能
slug: 374
date: 2021/03/21 12:20:50
updated: 2023/11/14 15:51:40
status: publish
author: admin
categories: 
  - 学习记录
tags: 
---


<div alt="潮男心博客 www.cnx0.com">
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">要知道，网站的打开速度取决于浏览器打开下载的网页文件大小。如果传输的页面内容文件减少，那你网站的打开速度一定会加快。特别是手机端的用户，打开网站速度受限于移动端网络，所以压缩网站页面内容显得至关重要。</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">gzip是一种非常流行的数据压缩方式。你可以在nginx配置中开启gzip来压缩网页文件。然后，这些文件又由浏览器解压缩，文件不会受任何。但是压缩文件是会占用服务器资源，所以最好压缩那些效果比较好的文件。比如文本文件压缩效果非常好，通常会缩小两倍多。而JPG或PNG这类文件，本身就已经进行格式压缩，所以再做二次压缩，效果并不是特别明显。</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">本文主要讲一下如何配置nginx来开启gzip压缩。</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">环境</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">ubuntu 20.04服务器</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">root权限或具有sudo特权的非root用户</span> 
	</p>
	<h3 style="text-indent:2em;color:#333333;font-family:Arial, Helvetica, &quot;background-color:#FFFFFF;">
		<span style="font-size:16px;">一、创建测试文件</span> 
	</h3>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">在这一步中，我们将在默认的Nginx目录中创建几个测试文件。稍后我们将使用这些文件来检查Nginx的默认行为是否进行gzip压缩，并测试配置更改是否具有预期的效果。</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">首先，创建几个测试文件，这些文件主要用来查看我们的gzip压缩效果。gzip是不会分析文件内容的，它主要通过文件扩展名来判断文件类型，如果还分析文件内容，那整个效率就会大大降低。所以我们可以创建一些图像文件、html文件和一些样式文件。</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">sudo truncate -s 1k /var/www/html/test.html</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">sudo truncate -s 1k /var/www/html/test.jpg</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">sudo truncate -s 1k /var/www/html/test.css</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">sudo truncate -s 1k /var/www/html/test.js</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">下一步是检查Nginx在使用我们刚创建的文件在全新安装中压缩请求的文件时的行为。</span> 
	</p>
	<h3 style="text-indent:2em;color:#333333;font-family:Arial, Helvetica, &quot;background-color:#FFFFFF;">
		<span style="font-size:16px;">二、命令方式查看压缩效果</span> 
	</h3>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">使用curl命令方式，添加标头Accept-Encoding: gzip，来查看各文件的压缩结果。</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">curl -H "Accept-Encoding: gzip" -I http://localhost/test.html</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">可以看到以下结果：</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Output</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">HTTP/1.1 200 OK</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Server: nginx/1.18.0 (Ubuntu)</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Date: Tue, 09 Feb 2021 19:04:25 GMT</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Content-Type: text/html</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Last-Modified: Tue, 09 Feb 2021 19:03:41 GMT</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Connection: keep-alive</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">ETag: W/"6022dc8d-400"</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Content-Encoding: gzip</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">在最后一行，出现Content-Encoding: gzip字样。说明服务器正在用gzip压缩来发送文件。默认情况下，nginx仅压缩html文件。所有在这个命令中可以看到文件做了压缩处理。但其它的文件格式，并未做压缩处理。</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">可以通过下面这条命令来验证我们刚才的说法。</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">curl -H "Accept-Encoding: gzip" -I http://localhost/test.jpg</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">再看一下结果，和之前的有所不同：</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Output</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">HTTP/1.1 200 OK</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Server: nginx/1.18.0 (Ubuntu)</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Date: Tue, 09 Feb 2021 19:05:49 GMT</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Content-Type: image/jpeg</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Content-Length: 1024</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Last-Modified: Tue, 09 Feb 2021 19:03:45 GMT</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Connection: keep-alive</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">ETag: "6022dc91-400"</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Accept-Ranges: bytes</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">输出结果中没有出现Content-Encoding: gzip，这意味着该文件并没有做任何的压缩。</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">你也可以使用这个方法来测试css等样式文件。</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">curl -H "Accept-Encoding: gzip" -I http://localhost/test.css</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">结果一样，没有出现Content-Encoding: gzip</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Output</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">HTTP/1.1 200 OK</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Server: nginx/1.18.0 (Ubuntu)</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Date: Tue, 09 Feb 2021 19:06:04 GMT</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Content-Type: text/css</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Content-Length: 1024</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Last-Modified: Tue, 09 Feb 2021 19:03:45 GMT</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Connection: keep-alive</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">ETag: "6022dc91-400"</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Accept-Ranges: bytes</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">三、配置Nginx开启gzip功能</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">本节主要操作相关配置，让gzip可以处理其它几种文件格式的压缩。</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">你可以使用nano或vim编辑nginx的配置文件。</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">sudo nano /etc/nginx/nginx.conf</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">找到gzip设置部分，如下所示：</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">/etc/nginx/nginx.conf</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">. . .</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">##</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;"># `gzip` Settings</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">#</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">#</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">gzip on;</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">gzip_disable "msie6";</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;"># gzip_vary on;</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;"># gzip_proxied any;</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;"># gzip_comp_level 6;</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;"># gzip_buffers 16 8k;</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;"># gzip_http_version 1.1;</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;"># gzip_types text/plain text/css application/json application/x-javascript text/xml application/xml application/xml+rss text/javascript;</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">. . .</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">因为我们用的是ubuntu 20.04。所以默认情况下，gzip是开启的。但有些设置无效，所以我们需要做一些修改：</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">通过取消注释行前面的#来启用其他设置(即，删除#符号)</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">添加gzip_min_length 256;参数，该参数是告诉nginx，不要去压缩小于256字节的文件，因为很小的文件没有太必要。压缩这类文件反而影响服务器效率。</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">在gzip_types参数中添加其他文件类型扩展名，这些文件类型可以是Web字体，图片、XML、JSON结构化数据或SVG图片文件。</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">应用这些更改之后，设置部分应如下所示：</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">/etc/nginx/nginx.conf</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">. . .</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">##</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;"># `gzip` Settings</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">#</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">#</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">gzip on;</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">gzip_disable "msie6";</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">gzip_vary on;</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">gzip_proxied any;</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">gzip_comp_level 6;</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">gzip_buffers 16 8k;</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">gzip_http_version 1.1;</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">gzip_min_length 256;</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">gzip_types</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">application/atom+xml</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">application/geo+json</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">application/javascript</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">application/x-javascript</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">application/json</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">application/ld+json</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">application/manifest+json</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">application/rdf+xml</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">application/rss+xml</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">application/xhtml+xml</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">application/xml</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">font/eot</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">font/otf</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">font/ttf</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">image/svg+xml</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">text/css</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">text/javascript</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">text/plain</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">text/xml;</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">. . .</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">保存并关闭文件以退出。要启用新配置，需要重新启动Nginx：</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">sudo systemctl restart nginx</span> 
	</p>
	<h3 style="text-indent:2em;color:#333333;font-family:Arial, Helvetica, &quot;background-color:#FFFFFF;">
		<span style="font-size:16px;">四、确保所有的配置正确</span> 
	</h3>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">重复之前的测试步骤，执行相应的命令请求：</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">curl -H "Accept-Encoding: gzip" -I http://localhost/test.html</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">因为html文件，之前已经默认开启压缩，所以这个命令执行结果保持不变：</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Output</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">HTTP/1.1 200 OK</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Server: nginx/1.18.0 (Ubuntu)</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Date: Tue, 09 Feb 2021 19:04:25 GMT</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Content-Type: text/html</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Last-Modified: Tue, 09 Feb 2021 19:03:41 GMT</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Connection: keep-alive</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">ETag: W/"6022dc8d-400"</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Content-Encoding: gzip</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">然后我们来测试一下之前未压缩的css样式表，看看结果会有什么变化：</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">curl -H "Accept-Encoding: gzip" -I http://localhost/test.css</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">可以看到gzip正在压缩文件：</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Output</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">HTTP/1.1 200 OK</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Server: nginx/1.18.0 (Ubuntu)</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Date: Tue, 09 Feb 2021 19:21:54 GMT</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Content-Type: text/css</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Last-Modified: Tue, 09 Feb 2021 19:03:45 GMT</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Connection: keep-alive</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Vary: Accept-Encoding</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">ETag: W/"6022dc91-400"</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Content-Encoding: gzip</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">我们可以用相同的方式测试一下jpg文件：</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">curl -H "Accept-Encoding: gzip" -I http://localhost/test.jpg</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">没有看到gzip压缩：</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Output</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">HTTP/1.1 200 OK</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Server: nginx/1.18.0 (Ubuntu)</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Date: Tue, 09 Feb 2021 19:25:40 GMT</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Content-Type: image/jpeg</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Content-Length: 1024</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Last-Modified: Tue, 09 Feb 2021 19:03:45 GMT</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Connection: keep-alive</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">ETag: "6022dc91-400"</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">Accept-Ranges: bytes</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">因为在之前的配置中，我们并没有添加 image/jpeg。</span> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">在这种情况下，我们已经在Nginx中成功配置了gzip。</span> 
	</p>
	<h3 style="text-indent:2em;color:#333333;font-family:Arial, Helvetica, &quot;background-color:#FFFFFF;">
		<span style="font-size:16px;">结论</span> 
	</h3>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">可以看出，gzip很容易配置，而且带来的速度提升也非常明显</span>
	</p>
	<p style="text-indent:unset;text-align:center;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<img src="https://www.kjsv.com/download/image/2021/03/21/20210321004142_966481.png" title="如何通过gzip和nginx来提高网站打开速度及整体性能 互联网 经验心得 第1张" alt="如何通过gzip和nginx来提高网站打开速度及整体性能 互联网 经验心得 第1张" border="0" style="width:unset;height:unset;" /> 
	</p>
	<p style="text-indent:2em;text-align:justify;color:#2A2A2A;font-family:Arial, Helvetica, &quot;font-size:20px;background-color:#FFFFFF;">
		<span style="font-size:16px;">搜索引擎也非常喜欢这类加载方式，如果想提高搜索引擎的排名，增加gzip是非常有必要的。</span> 
	</p>
</div>