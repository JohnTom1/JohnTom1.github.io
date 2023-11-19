---
layout: post
cid: 5
title: Layui hint is not a valid module
slug: 5
date: 2021/01/23 16:44:34
updated: 2023/11/14 15:51:40
status: publish
author: admin
categories: 
  - layui
tags: 
  - layui模板使用
---


<p style="box-sizing:border-box;outline:0px;margin-top:0px;margin-bottom:16px;padding:0px;font-size:16px;color:#4D4D4D;overflow:auto hidden;font-family:-apple-system, &quot;white-space:normal;background-color:#FFFFFF;line-height:26px !important;">
	在用layui引入第三方插件或者自定义模块时报此错误，找到原因是引入的模块没有遵循模块规范，记得检查一下最后有没有&nbsp;<span style="box-sizing:border-box;outline:0px;font-weight:700;overflow-wrap:break-word;">exports</span>&nbsp;暴露模块。
</p>
<h2 style="box-sizing:border-box;outline:0px;margin:8px 0px 16px;padding:0px;font-family:&quot;font-size:24px;color:#4F4F4F;line-height:32px;overflow-wrap:break-word;white-space:normal;background-color:#FFFFFF;">
	扩展一个 layui 模块
</h2>
<p style="box-sizing:border-box;outline:0px;margin-top:0px;margin-bottom:16px;padding:0px;font-size:16px;color:#4D4D4D;overflow:auto hidden;font-family:-apple-system, &quot;white-space:normal;background-color:#FFFFFF;line-height:26px !important;">
	第一步：确认模块名，假设为：<em style="box-sizing:border-box;outline:0px;overflow-wrap:break-word;">mymod</em>，然后新建一个&nbsp;<em style="box-sizing:border-box;outline:0px;overflow-wrap:break-word;">mymod.js</em>&nbsp;文件放入项目任意目录下（注意：不用放入layui目录）
</p>
<p style="box-sizing:border-box;outline:0px;margin-top:0px;margin-bottom:16px;padding:0px;font-size:16px;color:#4D4D4D;overflow:auto hidden;font-family:-apple-system, &quot;white-space:normal;background-color:#FFFFFF;line-height:26px !important;">
	第二步：编写 test.js 如下<span style="background-color:#FAFAFA;white-space:pre-wrap;"> </span>
</p>
<pre class="prettyprint lang-js linenums">/** 
 扩展一个test模块 
**/ 
layui.define(function(exports){ //提示：模块也可以依赖其它模块，如：layui.define('layer', callback); 
var obj = {
hello: function(str){
alert('Hello '+ (str||'mymod'));
}
};
//输出test接口 
exports('mymod', obj);
});
</pre>
第三步：设定扩展模块所在的目录，然后就可以在别的 JS 文件中使用了
<pre class="prettyprint lang-js linenums">//config的设置是全局的 
layui.config({
base: '/res/js/' //假设这是你存放拓展模块的根目录 
}).extend({ //设定模块别名 
mymod: 'mymod' //如果 mymod.js 是在根目录，也可以不用设定别名 
,mod1: 'admin/mod1' //相对于上述 base 目录的子目录 
});
//你也可以忽略 base 设定的根目录，直接在 extend 指定路径（主要：该功能为 layui 2.2.0 新增） 
layui.extend({
mod2: '{/}http://cdn.xxx.com/lib/mod2' // {/}的意思即代表采用自有路径，即不跟随 base 路径 
})
//使用拓展模块 
layui.use(['mymod', 'mod1'], function(){
var mymod = layui.mymod
,mod1 = layui.mod1
,mod2 = layui.mod2;
mymod.hello('World!'); //弹出 Hello World! 
});
参考</pre>
<p>
	<br />
</p>
<p style="box-sizing:border-box;outline:0px;margin-top:0px;margin-bottom:16px;padding:0px;font-size:16px;color:#4D4D4D;overflow:auto hidden;font-family:-apple-system, &quot;white-space:normal;background-color:#FFFFFF;line-height:26px !important;">
	<u style="box-sizing:border-box;outline:0px;overflow-wrap:break-word;"><a href="https://www.layui.com/doc/base/modules.html#extend" name="extend" style="box-sizing:border-box;outline:none;margin:0px;padding:0px;text-decoration-line:none;cursor:pointer;color:#6795B5;overflow-wrap:break-word;">扩展一个 layui 模块</a></u>
</p>
<h3 style="box-sizing:border-box;outline:0px;margin:8px 0px 16px;padding:0px;font-family:&quot;font-size:22px;color:#4F4F4F;line-height:30px;overflow-wrap:break-word;white-space:normal;background-color:#FFFFFF;">
	排错方法
</h3>
<ul style="box-sizing:border-box;outline:0px;margin:0px 0px 24px;padding:0px;list-style:none;font-size:16px;overflow-wrap:break-word;color:#333333;font-family:-apple-system, &quot;white-space:normal;background-color:#FFFFFF;">
	<li style="box-sizing:border-box;outline:0px;margin:8px 0px 0px 32px;padding:0px;list-style:disc;overflow-wrap:break-word;">
		是否重复引用了 layui.js？（我的问题出现在这重复应用了layui.js）
	</li>
	<li style="box-sizing:border-box;outline:0px;margin:8px 0px 0px 32px;padding:0px;list-style:disc;overflow-wrap:break-word;">
		文件加载的<span style="box-sizing:border-box;outline:0px;margin:0px;padding:0px;overflow-wrap:break-word;color:#F33B45;">路径</span>是否正确 ？（90%以上的原因，重点排查）
	</li>
	<li style="box-sizing:border-box;outline:0px;margin:8px 0px 0px 32px;padding:0px;list-style:disc;overflow-wrap:break-word;">
		有没有 exports 暴露模块？
	</li>
	<li style="box-sizing:border-box;outline:0px;margin:8px 0px 0px 32px;padding:0px;list-style:disc;overflow-wrap:break-word;">
		仔细看文档，仔细看文档，仔细看文档。
	</li>
	<li style="box-sizing:border-box;outline:0px;margin:8px 0px 0px 32px;padding:0px;list-style:disc;overflow-wrap:break-word;">
		转载自https://blog.csdn.net/qq6759/article/details/93718696
	</li>
</ul>