---
layout: post
cid: 441
title: Command &quot;python setup.py egg_info&quot; failed with error code 1 in /tmp/pip-build-*解决办法
slug: 441
date: 2021/11/16 18:05:57
updated: 2023/11/14 15:51:40
status: publish
author: admin
categories: 
  - python
tags: 
---


<h1 id="autoid-0-0-0" style="margin:10px 0px;padding:0px;font-size:28px;line-height:1.5;font-family:微软雅黑, PTSans, Arial, sans-serif;white-space:normal;background-color:#FFFFFF;">
	一、概述
</h1>
<p style="margin:10px auto;padding:0px;font-family:微软雅黑, PTSans, Arial, sans-serif;font-size:15px;white-space:normal;background-color:#FFFFFF;">
	我在使用pip3 install docker-compose的时候，出现了报错<br />
<pre class="prettyprint lang-py linenums">

        raise DistutilsError("Setup script exited with %s" % (v.args[0],))
    distutils.errors.DistutilsError: Setup script exited with error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
    
    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-23ykqx51/pynacl/
</pre>
<br />
	<p style="margin:10px auto;padding:0px;font-family:微软雅黑, PTSans, Arial, sans-serif;font-size:15px;white-space:normal;background-color:#FFFFFF;">
		百度了好久，最后终于找到了答案。
	</p>
	<div class="cnblogs_code" style="margin:5px 0px;padding:5px;background-color:#F5F5F5;border:1px solid #CCCCCC;overflow:auto;white-space:normal;font-family:&quot;">
<pre style="margin-top:0px;margin-bottom:0px;padding:0px;overflow:auto;font-family:&quot;overflow-wrap:break-word;white-space:pre-wrap;">pip3 <span style="margin:0px;padding:0px;line-height:1.5;color:#0000FF;">install</span> --upgrade pip</pre>
	</div>
	<p style="margin:10px auto;padding:0px;font-family:微软雅黑, PTSans, Arial, sans-serif;font-size:15px;white-space:normal;background-color:#FFFFFF;">
		然后再执行pip3 install <span style="font-family:微软雅黑, PTSans, Arial, sans-serif;font-size:15px;white-space:normal;background-color:#FFFFFF;">docker-compose</span>，就没有提示了。<br />
参考链接https://www.cnblogs.com/xiao987334176/p/12600835.html
	</p>
</p>