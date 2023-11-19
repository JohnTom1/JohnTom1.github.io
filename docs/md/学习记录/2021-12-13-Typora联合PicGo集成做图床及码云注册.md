---
layout: post
cid: 447
title: Typora联合PicGo集成做图床及码云注册
slug: 447
date: 2021/12/13 12:31:37
updated: 2023/11/14 15:51:40
status: publish
author: admin
categories: 
  - 学习记录
tags: 
  - typora
---


<ul class="ul-list" cid="n53" mdtype="list" data-mark="-" style="box-sizing:border-box;margin:30px 0px 0.8em;padding-left:30px;position:relative;color:#333333;font-family:&quot;font-size:16px;white-space:normal;">
	<li class="md-list-item" cid="n54" mdtype="list_item" style="box-sizing:border-box;margin:0px;position:relative;">
		<p cid="n55" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0px;margin-bottom:0.5rem;white-space:pre-wrap;position:relative;">
			<span md-inline="plain" class="md-plain md-expand" style="box-sizing:border-box;">typora支持将Ctrl+v粘贴到里面的图片直接上传到指定的服务器，使用码云当作云图床</span> 
		</p>
		<h2 cid="n56" mdtype="heading" class="md-end-block md-heading" style="box-sizing:border-box;break-after:avoid-page;break-inside:avoid;orphans:4;font-size:1.75em;margin-top:1rem;margin-bottom:1rem;position:relative;line-height:1.225;cursor:text;border-bottom:1px solid #EEEEEE;white-space:pre-wrap;">
			<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">1.下载PicGo</span> 
		</h2>
		<p cid="n57" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.5rem;margin-bottom:0.5rem;white-space:pre-wrap;position:relative;">
			<span md-inline="tab" class="md-tab" style="box-sizing:border-box;display:inline-block;white-space:pre;"> </span><span md-inline="url" class="md-link md-pair-s" spellcheck="false" style="box-sizing:border-box;word-break:break-all;"><a href="https://molunerfinn.com/PicGo/" style="box-sizing:border-box;cursor:pointer;color:#4183C4;-webkit-user-drag:none;">https://molunerfinn.com/PicGo/</a></span> 
		</p>
		<p cid="n58" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.5rem;margin-bottom:0.5rem;white-space:pre-wrap;position:relative;">
			<span md-inline="image" data-src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529162654804.png" class="md-image md-img-loaded" style="box-sizing:border-box;min-width:10px;min-height:10px;position:relative;word-break:break-all;font-family:monospace;vertical-align:top;display:inline-block;width:686px;"><img referrerpolicy="no-referrer" alt="image-20200529162654804" src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529162654804.png" style="box-sizing:border-box;border-right:4px solid transparent;border-left:2px solid transparent;vertical-align:middle;max-width:100%;image-orientation:from-image;cursor:default;display:block;margin:auto;" /></span> 
		</p>
		<h2 cid="n59" mdtype="heading" class="md-end-block md-heading" style="box-sizing:border-box;break-after:avoid-page;break-inside:avoid;orphans:4;font-size:1.75em;margin-top:1rem;margin-bottom:1rem;position:relative;line-height:1.225;cursor:text;border-bottom:1px solid #EEEEEE;white-space:pre-wrap;">
			<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">2.安装下载的PicGo，并根据下图所示配置(必须安装nodejs,否则插件一直是“安装中”，据说最新版本的PicGo已经有提示了，我没试)</span> 
		</h2>
		<p cid="n60" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.5rem;margin-bottom:0.5rem;white-space:pre-wrap;position:relative;">
			<span md-inline="image" data-src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529162847746.png" class="md-image md-img-loaded" style="box-sizing:border-box;min-width:10px;min-height:10px;position:relative;word-break:break-all;font-family:monospace;vertical-align:top;display:inline-block;width:686px;"><img referrerpolicy="no-referrer" alt="image-20200529162847746" src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529162847746.png" style="box-sizing:border-box;border-right:4px solid transparent;border-left:2px solid transparent;vertical-align:middle;max-width:100%;image-orientation:from-image;cursor:default;display:block;margin:auto;" /></span> 
		</p>
		<h2 cid="n61" mdtype="heading" class="md-end-block md-heading" style="box-sizing:border-box;break-after:avoid-page;break-inside:avoid;orphans:4;font-size:1.75em;margin-top:1rem;margin-bottom:1rem;position:relative;line-height:1.225;cursor:text;border-bottom:1px solid #EEEEEE;white-space:pre-wrap;">
			<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">3.注册码云-&gt;创建仓库</span> 
		</h2>
		<p cid="n62" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.5rem;margin-bottom:0.5rem;white-space:pre-wrap;position:relative;">
			<span md-inline="url" class="md-link md-pair-s" spellcheck="false" style="box-sizing:border-box;word-break:break-all;"><a href="https://gitee.com/" style="box-sizing:border-box;cursor:pointer;color:#4183C4;-webkit-user-drag:none;">https://gitee.com/</a></span> 
		</p>
	</li>
</ul>
<p cid="n63" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="image" data-src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529163151150.png" class="md-image md-img-loaded" style="box-sizing:border-box;min-width:10px;min-height:10px;position:relative;word-break:break-all;font-family:monospace;vertical-align:top;display:inline-block;width:716px;"><img referrerpolicy="no-referrer" alt="image-20200529163151150" src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529163151150.png" style="box-sizing:border-box;border-right:4px solid transparent;border-left:2px solid transparent;vertical-align:middle;max-width:100%;image-orientation:from-image;cursor:default;display:block;margin:auto;" /></span> 
</p>
<h2 cid="n64" mdtype="heading" class="md-end-block md-heading" style="box-sizing:border-box;break-after:avoid-page;break-inside:avoid;orphans:4;font-size:1.75em;margin-top:1rem;margin-bottom:1rem;position:relative;line-height:1.225;cursor:text;border-bottom:1px solid #EEEEEE;white-space:pre-wrap;color:#333333;font-family:&quot;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">4.创建码云私人令牌 </span><span md-inline="strong" class="md-pair-s " style="box-sizing:border-box;">生成令牌后要记住，关了就不能再显示了</span> 
</h2>
<p cid="n65" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="image" data-src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529163852671.png" class="md-image md-img-loaded" style="box-sizing:border-box;min-width:10px;min-height:10px;position:relative;word-break:break-all;font-family:monospace;vertical-align:top;display:inline-block;width:716px;"><img referrerpolicy="no-referrer" alt=" " src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529163852671.png" style="box-sizing:border-box;border-right:4px solid transparent;border-left:2px solid transparent;vertical-align:middle;max-width:100%;image-orientation:from-image;cursor:default;display:block;margin:auto;" /></span> 
</p>
<h2 cid="n66" mdtype="heading" class="md-end-block md-heading" style="box-sizing:border-box;break-after:avoid-page;break-inside:avoid;orphans:4;font-size:1.75em;margin-top:1rem;margin-bottom:1rem;position:relative;line-height:1.225;cursor:text;border-bottom:1px solid #EEEEEE;white-space:pre-wrap;color:#333333;font-family:&quot;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">5.配置PicGo程序</span> 
</h2>
<p cid="n67" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">打开程序-&gt;左侧图床设置-&gt;gitee</span> 
</p>
<p cid="n68" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="image" data-src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529164602947.png" class="md-image md-img-loaded" style="box-sizing:border-box;min-width:10px;min-height:10px;position:relative;word-break:break-all;font-family:monospace;vertical-align:top;display:inline-block;width:716px;"><img referrerpolicy="no-referrer" alt="image-20200529164602947" src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529164602947.png" style="box-sizing:border-box;border-right:4px solid transparent;border-left:2px solid transparent;vertical-align:middle;max-width:100%;image-orientation:from-image;cursor:default;display:block;margin:auto;" /></span> 
</p>
<h2 cid="n69" mdtype="heading" class="md-end-block md-heading" style="box-sizing:border-box;break-after:avoid-page;break-inside:avoid;orphans:4;font-size:1.75em;margin-top:1rem;margin-bottom:1rem;position:relative;line-height:1.225;cursor:text;border-bottom:1px solid #EEEEEE;white-space:pre-wrap;color:#333333;font-family:&quot;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">6.上一步设置默认图床和确认后，即可在上传区测试，能上传成功证明配置完成</span> 
</h2>
<p cid="n70" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="image" data-src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529164723929.png" class="md-image md-img-loaded" style="box-sizing:border-box;min-width:10px;min-height:10px;position:relative;word-break:break-all;font-family:monospace;vertical-align:top;display:inline-block;width:716px;"><img referrerpolicy="no-referrer" alt="image-20200529164723929" src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529164723929.png" style="box-sizing:border-box;border-right:4px solid transparent;border-left:2px solid transparent;vertical-align:middle;max-width:100%;image-orientation:from-image;cursor:default;display:block;margin:auto;" /></span> 
</p>
<h2 cid="n71" mdtype="heading" class="md-end-block md-heading" style="box-sizing:border-box;break-after:avoid-page;break-inside:avoid;orphans:4;font-size:1.75em;margin-top:1rem;margin-bottom:1rem;position:relative;line-height:1.225;cursor:text;border-bottom:1px solid #EEEEEE;white-space:pre-wrap;color:#333333;font-family:&quot;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">7.Typora集成PicGo</span> 
</h2>
<h3 cid="n72" mdtype="heading" class="md-end-block md-heading" style="box-sizing:border-box;break-after:avoid-page;break-inside:avoid;orphans:4;font-size:1.5em;margin-top:1rem;margin-bottom:1rem;position:relative;line-height:1.43;cursor:text;white-space:pre-wrap;color:#333333;font-family:&quot;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">7-1 打开Typora -&gt;文件 -&gt; 偏好设置</span> 
</h3>
<h3 cid="n73" mdtype="heading" class="md-end-block md-heading" style="box-sizing:border-box;break-after:avoid-page;break-inside:avoid;orphans:4;font-size:1.5em;margin-top:1rem;margin-bottom:1rem;position:relative;line-height:1.43;cursor:text;white-space:pre-wrap;color:#333333;font-family:&quot;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">7-2 参考下图</span> 
</h3>
<p cid="n74" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="image" data-src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529165022665.png" class="md-image md-img-loaded" style="box-sizing:border-box;min-width:10px;min-height:10px;position:relative;word-break:break-all;font-family:monospace;vertical-align:top;display:inline-block;width:716px;"><img referrerpolicy="no-referrer" alt="image-20200529165022665" src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529165022665.png" style="box-sizing:border-box;border-right:4px solid transparent;border-left:2px solid transparent;vertical-align:middle;max-width:100%;image-orientation:from-image;cursor:default;display:block;margin:auto;" /></span> 
</p>
<h3 cid="n75" mdtype="heading" class="md-end-block md-heading" style="box-sizing:border-box;break-after:avoid-page;break-inside:avoid;orphans:4;font-size:1.5em;margin-top:1rem;margin-bottom:1rem;position:relative;line-height:1.43;cursor:text;white-space:pre-wrap;color:#333333;font-family:&quot;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">7-3 验证通过后即集成成功，在Typora中粘贴截图即可自动上传到配置的码云</span> 
</h3>
<h2 cid="n76" mdtype="heading" class="md-end-block md-heading" style="box-sizing:border-box;break-after:avoid-page;break-inside:avoid;orphans:4;font-size:1.75em;margin-top:1rem;margin-bottom:1rem;position:relative;line-height:1.225;cursor:text;border-bottom:1px solid #EEEEEE;white-space:pre-wrap;color:#333333;font-family:&quot;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">8.PicGo上传异常情况</span> 
</h2>
<ul class="ul-list" cid="n77" mdtype="list" data-mark="-" style="box-sizing:border-box;margin:0.8em 0px;padding-left:30px;position:relative;color:#333333;font-family:&quot;font-size:16px;white-space:normal;">
	<li class="md-list-item" cid="n78" mdtype="list_item" style="box-sizing:border-box;margin:0px;position:relative;">
		<p cid="n79" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0px;margin-bottom:0.5rem;white-space:pre-wrap;position:relative;">
			<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">Typora默认是通过</span><span md-inline="strong" class="md-pair-s " style="box-sizing:border-box;"><strong style="box-sizing:border-box;">36677</strong></span><span md-inline="plain" class="md-plain" style="box-sizing:border-box;">端口上传，打开PicGo-&gt;PicGo设置-&gt;设置Server.看里面的端口是否是36677，这个端口可能会变化，如果不是手动改成36677即可</span> 
		</p>
	</li>
</ul>
<p cid="n80" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="image" data-src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529165410221.png" class="md-image md-img-loaded" style="box-sizing:border-box;min-width:10px;min-height:10px;position:relative;word-break:break-all;font-family:monospace;vertical-align:top;display:inline-block;width:716px;"><img referrerpolicy="no-referrer" alt="image-20200529165410221" src="https://gitee.com/RollBack2010/blogsimg/raw/master/img/image-20200529165410221.png" style="box-sizing:border-box;border-right:4px solid transparent;border-left:2px solid transparent;vertical-align:middle;max-width:100%;image-orientation:from-image;cursor:default;display:block;margin:auto;" /></span> 
</p>
<p cid="n51" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">记录一下使用npm安装picgo-plugin-gitee-uploader</span> 
</p>
<p cid="n18" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">1.前言</span><span md-inline="softbreak" class="md-softbreak" style="box-sizing:border-box;"> </span><span md-inline="plain" class="md-plain" style="box-sizing:border-box;">平时使用Typora，然后利用PicGo图片床自动上传图片，使用的是gitee的自建图床，具体攻略可参见PicGo+gitee搭建个人图床</span> 
</p>
<p cid="n3" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">Gitee图床不是PicGo的列表图床，需要通过插件设置 来添加，但是必须安装Node.js之后才能安装PicGo的插件，因为PicGo要使用npm来安装插件。需要安装的见下面地址：Node.js下载地址</span><span md-inline="softbreak" class="md-softbreak" style="box-sizing:border-box;"> </span><span md-inline="plain" class="md-plain" style="box-sizing:border-box;">安装完Node.js，在PicGo插件设置里搜索 gitee，应该能出两个选项，一个是 picgo-plugin-gitee ，另外一个是picgo-plugin-gitee-uploader ，重点来了，可能最近npm那边的搜索服务崩了，搜索gitee居然不出任何结果，崩溃！</span> 
</p>
<p cid="n4" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">2.手动安装PicGo插件</span><span md-inline="softbreak" class="md-softbreak" style="box-sizing:border-box;"> </span><span md-inline="plain" class="md-plain" style="box-sizing:border-box;">所以本文记录一下如何手动安装PicGo插件！</span><span md-inline="softbreak" class="md-softbreak" style="box-sizing:border-box;"> </span><span md-inline="plain" class="md-plain" style="box-sizing:border-box;">首先确保安装Node.js, Win+R键 ，输入 cmd 调用 命令行窗口， 输入 npm -v 能显示 版本号，说明你npm可以使用</span> 
</p>
<p cid="n26" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="image" data-src="https://gitee.com/jiandanyidianjiuhao/cloudimages/raw/master/img/image-20211213122239939.png" class="md-image md-img-loaded" style="box-sizing:border-box;min-width:10px;min-height:10px;position:relative;word-break:break-all;font-family:monospace;vertical-align:top;display:inline-block;width:716px;"><img referrerpolicy="no-referrer" alt="image-20211213122239939" src="https://gitee.com/jiandanyidianjiuhao/cloudimages/raw/master/img/image-20211213122239939.png" style="box-sizing:border-box;border-right:4px solid transparent;border-left:2px solid transparent;vertical-align:middle;max-width:100%;image-orientation:from-image;cursor:default;display:block;margin:auto;" /></span> 
</p>
<p cid="n5" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">然后 转到 windows 配置目录在C:\Users\XXX\AppData\Roaming\picgo 下 ，XXX 为 电脑的用户名，根据自己的情况修改即可</span><span md-inline="softbreak" class="md-softbreak" style="box-sizing:border-box;"> </span><span md-inline="plain" class="md-plain" style="box-sizing:border-box;">cd C:\Users\XXX\AppData\Roaming\picgo</span> 
</p>
<p cid="n44" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="image" data-src="https://gitee.com/jiandanyidianjiuhao/cloudimages/raw/master/img/image-20211213122305798.png" class="md-image md-img-loaded" style="box-sizing:border-box;min-width:10px;min-height:10px;position:relative;word-break:break-all;font-family:monospace;vertical-align:top;display:inline-block;width:716px;"><img referrerpolicy="no-referrer" alt="image-20211213122305798" src="https://gitee.com/jiandanyidianjiuhao/cloudimages/raw/master/img/image-20211213122305798.png" style="box-sizing:border-box;border-right:4px solid transparent;border-left:2px solid transparent;vertical-align:middle;max-width:100%;image-orientation:from-image;cursor:default;display:block;margin:auto;" /></span> 
</p>
<p cid="n6" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">最后在该目录下，使用npm手动安装gitee图床，命令如下：</span><span md-inline="softbreak" class="md-softbreak" style="box-sizing:border-box;"> </span><span md-inline="plain" class="md-plain" style="box-sizing:border-box;">npm install picgo-plugin-gitee-uploader ，然后重启picgo即可。</span> 
</p>
<p cid="n7" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">也可以安装其他的插件，PicGo插件 清单</span> 
</p>
<p cid="n8" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">大功告成，额，只是安装插件成功，想成功使用gitee图床还需要一系列的配置，具体见 前言部分的 参考链接，不在赘述啦。</span> 
</p>
<p cid="n9" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="plain" class="md-plain" style="box-sizing:border-box;">最后上个效果图！</span> 
</p>
<p cid="n48" mdtype="paragraph" class="md-end-block md-p" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="image" data-src="https://gitee.com/jiandanyidianjiuhao/cloudimages/raw/master/img/image-20211213122347705.png" class="md-image md-img-loaded" style="box-sizing:border-box;min-width:10px;min-height:10px;position:relative;word-break:break-all;font-family:monospace;vertical-align:top;"><img referrerpolicy="no-referrer" alt="image-20211213122347705" src="https://gitee.com/jiandanyidianjiuhao/cloudimages/raw/master/img/image-20211213122347705.png" style="box-sizing:border-box;border-right:4px solid transparent;border-left:2px solid transparent;vertical-align:middle;max-width:100%;image-orientation:from-image;cursor:default;" /><br />
</span><span md-inline="plain" class="md-plain" style="box-sizing:border-box;">原文链接：</span><span md-inline="url" class="md-link md-pair-s" spellcheck="false" style="box-sizing:border-box;word-break:break-all;"><a href="https://blog.csdn.net/lunhui601/article/details/107722580" style="box-sizing:border-box;cursor:pointer;color:#4183C4;-webkit-user-drag:none;">https://blog.csdn.net/lunhui601/article/details/107722580</a></span> <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="https://zhuanlan.zhihu.com/p/112954321" target="_blank">&nbsp;https://zhuanlan.zhihu.com/p/112954321</a> 
</p>
<p cid="n122" mdtype="paragraph" class="md-end-block md-p md-focus" style="box-sizing:border-box;line-height:inherit;orphans:4;margin-top:0.8em;margin-bottom:0.8em;white-space:pre-wrap;position:relative;color:#333333;font-family:&quot;font-size:16px;">
	<span md-inline="plain" class="md-plain md-expand" style="box-sizing:border-box;">只做记录，注明了出处如侵权联删。</span> 
</p>