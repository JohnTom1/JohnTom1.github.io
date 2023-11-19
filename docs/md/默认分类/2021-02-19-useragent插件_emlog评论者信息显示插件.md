---
layout: post
cid: 156
title: useragent插件 emlog评论者信息显示插件
slug: 156
date: 2021/02/19 16:19:22
updated: 2023/11/14 15:51:40
status: publish
author: admin
categories: 
  - 默认分类
tags: 
  - emlog插件
---


<header class="panel-header" style="box-sizing:border-box;line-height:38px;background:#FFFFFF;">
<h2 class="post-title" style="box-sizing:border-box;font-family:inherit;font-weight:400;line-height:34px;color:#666666;margin-top:0px;margin-bottom:10px;font-size:18px;text-align:center;border-left:5px solid #45B6F7;margin-left:-1px;overflow:hidden;text-overflow:ellipsis;width:758px;height:45px;-webkit-box-reflect:below -37px -webkit-gradient(linear, 0% 0%, 0% 100%, from(transparent), color-stop(0.1, transparent), to(rgba(255, 255, 255, 0.3)));">
	<br />
</h2>
</header><section class="context" style="box-sizing:border-box;padding:15px;overflow-wrap:break-word;min-height:100px;">
<p style="box-sizing:border-box;margin-top:0px;margin-bottom:10px;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;">
	<span style="box-sizing:border-box;font-size:16px;">&nbsp; 此插件是叶靖发布的第一个插件，我自己在用，希望有需要的朋友看看！</span>
</p>
<p style="box-sizing:border-box;margin-top:0px;margin-bottom:10px;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;">
	<span style="box-sizing:border-box;font-size:16px;"></span>
</p>
<pre class="prettyprint lang-html linenums" style="box-sizing:border-box;overflow:auto;font-family:Menlo, Monaco, Consolas, &quot;font-size:13px;padding:9.5px;margin-top:0px;margin-bottom:10px;line-height:1.42857;color:#333333;word-break:break-all;overflow-wrap:break-word;background-color:#F5F5F5;border:1px solid #CCCCCC;border-radius:4px;position:relative;">功能介绍：<span class="copy_code" style="box-sizing:border-box;position:absolute;top:0px;right:0px;padding:5px 10px;background:#EA5A47;color:#FFFFFF;cursor:pointer;"></span>
<div class="zclip" id="zclip-ZeroClipboardMovie_1" style="box-sizing:border-box;position:absolute;right:0px;top:0px;width:46px;height:28px;z-index:99;">
	
</div>
</pre>
<span style="box-sizing:border-box;color:#333333;font-family:&quot;white-space:normal;background-color:#FFFFFF;font-size:16px;">&nbsp; 在留言列表评论者这里，显示你的浏览器和操作系统，支持以下主流浏览器和系统，以及评论者等级及会员认证、管理员认证。</span>
<pre class="prettyprint lang-html linenums" style="box-sizing:border-box;overflow:auto;font-family:Menlo, Monaco, Consolas, &quot;font-size:13px;padding:9.5px;margin-top:0px;margin-bottom:10px;line-height:1.42857;color:#333333;word-break:break-all;overflow-wrap:break-word;background-color:#F5F5F5;border:1px solid #CCCCCC;border-radius:4px;position:relative;">安装使用：<span class="copy_code" style="box-sizing:border-box;position:absolute;top:0px;right:0px;padding:5px 10px;background:#EA5A47;color:#FFFFFF;cursor:pointer;"></span>
<div class="zclip" id="zclip-ZeroClipboardMovie_2" style="box-sizing:border-box;position:absolute;right:0px;top:0px;width:46px;height:28px;z-index:99;">
	
</div>
</pre>
<span style="box-sizing:border-box;color:#333333;font-family:&quot;white-space:normal;background-color:#FFFFFF;font-size:16px;">1.下载插件并解压；</span><br style="box-sizing:border-box;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;" />
<span style="box-sizing:border-box;color:#333333;font-family:&quot;white-space:normal;background-color:#FFFFFF;font-size:16px;">2.上传至emlog插件根目录并后台激活此插件；</span><br style="box-sizing:border-box;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;" />
<span style="box-sizing:border-box;color:#333333;font-family:&quot;white-space:normal;background-color:#FFFFFF;font-size:16px;">3.打开你所用模板中的module.php，找到评论列表模块和子评论列表模块，在foreach和endforeach之间的合适位置插入一段显示浏览器和操作系统的代码。以官方模板为例：</span><br style="box-sizing:border-box;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;" />
<pre class="prettyprint lang-cs linenums" style="box-sizing:border-box;overflow:auto;font-family:Menlo, Monaco, Consolas, &quot;font-size:13px;padding:9.5px;margin-top:0px;margin-bottom:10px;line-height:1.42857;color:#333333;word-break:break-all;overflow-wrap:break-word;background-color:#F5F5F5;border:1px solid #CCCCCC;border-radius:4px;position:relative;">找到评论列表模块和子评论列表模块的&lt;?php echo $comment['poster']; ?&gt;，在这之后
1.0~1.1版添加：
&lt;?php if(function_exists('display_useragent')){display_useragent($comment['cid']);} ?&gt;
1.2版以后添加：
&lt;?php if(function_exists('display_useragent')){display_useragent($comment['cid'],$comment['mail']);} ?&gt;<span class="copy_code" style="box-sizing:border-box;position:absolute;top:0px;right:0px;padding:5px 10px;background:#EA5A47;color:#FFFFFF;cursor:pointer;"></span>
<div class="zclip" id="zclip-ZeroClipboardMovie_3" style="box-sizing:border-box;position:absolute;right:0px;top:0px;width:46px;height:28px;z-index:99;">
	
</div>
</pre>
<pre class="prettyprint lang-cs linenums" style="box-sizing:border-box;overflow:auto;font-family:Menlo, Monaco, Consolas, &quot;font-size:13px;padding:9.5px;margin-top:0px;margin-bottom:10px;line-height:1.42857;color:#333333;word-break:break-all;overflow-wrap:break-word;background-color:#F5F5F5;border:1px solid #CCCCCC;border-radius:4px;position:relative;">说明：<span class="copy_code" style="box-sizing:border-box;position:absolute;top:0px;right:0px;padding:5px 10px;background:#EA5A47;color:#FFFFFF;cursor:pointer;"></span>
<div class="zclip" id="zclip-ZeroClipboardMovie_4" style="box-sizing:border-box;position:absolute;right:0px;top:0px;width:46px;height:28px;z-index:99;">
	
</div>
</pre>
<p style="box-sizing:border-box;margin-top:0px;margin-bottom:10px;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;">
	<br />
</p>
<p style="box-sizing:border-box;margin-top:0px;margin-bottom:10px;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;">
	<span style="box-sizing:border-box;font-size:16px;">1.这段代码放在侧边栏也是可行的，只需加在module.php的最新评论模块的foreach和endforeach之间的合适位置即可。</span><br style="box-sizing:border-box;" />
<span style="box-sizing:border-box;font-size:16px;">2.因为emlog没有记录访客useragent的相关字段，启用插件会新建该字段。而启用插件以前的评论将不显示相应的浏览器和操作系统。</span><br style="box-sizing:border-box;" />
<span style="box-sizing:border-box;font-size:16px;">3.如果不想使用此插件，默认会保留useragent，如果你要删除该字段，请在get_useragent_callback.php中取消callback_rm函数的所有注释符号。</span>
</p>
<p style="box-sizing:border-box;margin-top:0px;margin-bottom:10px;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;">
	<span style="box-sizing:border-box;font-size:16px;"></span>
</p>
<pre class="prettyprint lang-html linenums" style="box-sizing:border-box;overflow:auto;font-family:Menlo, Monaco, Consolas, &quot;font-size:13px;padding:9.5px;margin-top:0px;margin-bottom:10px;line-height:1.42857;color:#333333;word-break:break-all;overflow-wrap:break-word;background-color:#F5F5F5;border:1px solid #CCCCCC;border-radius:4px;position:relative;">更新记录<span class="copy_code" style="box-sizing:border-box;position:absolute;top:0px;right:0px;padding:5px 10px;background:#EA5A47;color:#FFFFFF;cursor:pointer;"></span>
<div class="zclip" id="zclip-ZeroClipboardMovie_5" style="box-sizing:border-box;position:absolute;right:0px;top:0px;width:46px;height:28px;z-index:99;">
	
</div>
</pre>
<span style="box-sizing:border-box;color:#333333;font-family:&quot;white-space:normal;background-color:#FFFFFF;font-size:16px;">1.3.1版更新</span><br style="box-sizing:border-box;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;" />
<span style="box-sizing:border-box;color:#333333;font-family:&quot;white-space:normal;background-color:#FFFFFF;font-size:16px;">修复数据库前缀错误问题 （谢谢 贝壳iT 找出问题）</span><br style="box-sizing:border-box;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;" />
<span style="box-sizing:border-box;color:#333333;font-family:&quot;white-space:normal;background-color:#FFFFFF;font-size:16px;">1.3版更新</span><br style="box-sizing:border-box;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;" />
<span style="box-sizing:border-box;color:#333333;font-family:&quot;white-space:normal;background-color:#FFFFFF;font-size:16px;">修复多核浏览器识别错误问题</span><br style="box-sizing:border-box;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;" />
<span style="box-sizing:border-box;color:#333333;font-family:&quot;white-space:normal;background-color:#FFFFFF;font-size:16px;">1.2版更新说明</span><br style="box-sizing:border-box;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;" />
<span style="box-sizing:border-box;color:#333333;font-family:&quot;white-space:normal;background-color:#FFFFFF;font-size:16px;">支持显示 评论者等级及会员认证、管理员认证。</span><br style="box-sizing:border-box;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;" />
<span style="box-sizing:border-box;color:#333333;font-family:&quot;white-space:normal;background-color:#FFFFFF;font-size:16px;">1.1版更新说明：</span><br style="box-sizing:border-box;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;" />
<span style="box-sizing:border-box;color:#333333;font-family:&quot;white-space:normal;background-color:#FFFFFF;font-size:16px;">兼容部分定制安卓机。</span><br style="box-sizing:border-box;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;" />
<pre class="prettyprint lang-html linenums" style="box-sizing:border-box;overflow:auto;font-family:Menlo, Monaco, Consolas, &quot;font-size:13px;padding:9.5px;margin-top:0px;margin-bottom:10px;line-height:1.42857;color:#333333;word-break:break-all;overflow-wrap:break-word;background-color:#F5F5F5;border:1px solid #CCCCCC;border-radius:4px;position:relative;">下载：<span class="copy_code" style="box-sizing:border-box;position:absolute;top:0px;right:0px;padding:5px 10px;background:#EA5A47;color:#FFFFFF;cursor:pointer;"></span>
<div class="zclip" id="zclip-ZeroClipboardMovie_6" style="box-sizing:border-box;position:absolute;right:0px;top:0px;width:46px;height:28px;z-index:99;">
	
</div>
</pre>
<p style="box-sizing:border-box;margin-top:0px;margin-bottom:10px;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;">
	<span style="box-sizing:border-box;font-size:14px;">百度网盘下载地址：<a href="http://pan.baidu.com/s/1dDpQaop" target="_blank" style="box-sizing:border-box;background-color:transparent;color:#666666;text-decoration-line:none;cursor:url(&quot;border-bottom:1px solid #45B6F7;">http://pan.baidu.com/s/1dDpQaop</a></span>
</p>
<p style="box-sizing:border-box;margin-top:0px;margin-bottom:10px;color:#333333;font-family:&quot;font-size:13px;white-space:normal;background-color:#FFFFFF;">
	<span style="box-sizing:border-box;font-size:14px;line-height:21px;">360 网盘下载地址：</span><a href="http://yunpan.cn/cjjdbiQSpEJ7A" target="_blank" style="box-sizing:border-box;background-color:transparent;color:#666666;text-decoration-line:none;cursor:url(&quot;border-bottom:1px solid #45B6F7;">http://yunpan.cn/cjjdbiQSpEJ7A</a>&nbsp;（提取码：e82e）
</p>
<div>
	转载自：https://www.sogou.com/link?url=hedJjaC291OODab7684SHWqp8gn1KrtyhbAx2xDx79St5pUc3zy0dg..
</div>
</section>