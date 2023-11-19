---
layout: post
cid: 11
title: layui利用自带的验证规则验证弹窗（弹出层）中的form表单
slug: 11
date: 2021/02/01 22:07:23
updated: 2023/11/14 15:51:40
status: publish
author: admin
categories: 
  - layui
tags: 
  - layui
  - php
---


<h1 style="box-sizing:border-box;outline:0px;margin:8px 0px 16px;padding:0px;font-family:&quot;font-size:28px;color:#4F4F4F;line-height:36px;overflow-wrap:break-word;white-space:normal;background-color:#FFFFFF;">
	前言
</h1>
<p style="box-sizing:border-box;outline:0px;margin-top:0px;margin-bottom:16px;padding:0px;font-size:16px;color:#4D4D4D;overflow:auto hidden;font-family:-apple-system, &quot;white-space:normal;background-color:#FFFFFF;line-height:26px !important;">
	在使用layui弹出层时，想着在点击弹出层中“确定”按钮时，也能触发弹出层中form表单的验证。最后找到一个还算可以的答案，参考<a href="https://fly.layui.com/jie/5581/" style="box-sizing:border-box;outline:none;margin:0px;padding:0px;text-decoration-line:none;cursor:pointer;color:#6795B5;overflow-wrap:break-word;">https://fly.layui.com/jie/5581/</a>，结合自己的理解，实现了这个功能。
</p>
<h1 style="box-sizing:border-box;outline:0px;margin:8px 0px 16px;padding:0px;font-family:&quot;font-size:28px;color:#4F4F4F;line-height:36px;overflow-wrap:break-word;white-space:normal;background-color:#FFFFFF;">
	具体实现
</h1>
<p style="box-sizing:border-box;outline:0px;margin-top:0px;margin-bottom:16px;padding:0px;font-size:16px;color:#4D4D4D;overflow:auto hidden;font-family:-apple-system, &quot;white-space:normal;background-color:#FFFFFF;line-height:26px !important;">
	整体思路就是在弹出层form表单页面中设置一个隐藏的提交按钮，然后在layer弹出层点击“确定”按钮时，找到form表单中隐藏的提交按钮，触发点击事件，即可实现验证功能。
</p>
<p style="box-sizing:border-box;outline:0px;margin-top:0px;margin-bottom:16px;padding:0px;font-size:16px;color:#4D4D4D;overflow:auto hidden;font-family:-apple-system, &quot;white-space:normal;background-color:#FFFFFF;line-height:26px !important;">
	这里使用的是客户信息html文件：customform.html
</p>
<p style="box-sizing:border-box;outline:0px;margin-top:0px;margin-bottom:16px;padding:0px;font-size:16px;color:#4D4D4D;overflow:auto hidden;font-family:-apple-system, &quot;white-space:normal;background-color:#FFFFFF;line-height:26px !important;">
	<span style="box-sizing:border-box;outline:0px;font-weight:700;overflow-wrap:break-word;background-color:#E56600;">重点查看新增客户的js代码段和form表单中设置的隐藏提交按钮即可<br />
父页面js相关代码如下： </span> 
</p>
<pre class="brush:js; toolbar: true; auto-links: true;"> //事件
        var active = {
            batchdel: function(){
                layer.confirm('确定恢复吗？', function () {
                    $.get("{:url('Customer/unDelete')}");


                    //执行 Ajax 后重载
                    /*
                    admin.req({
                      url: 'xxx'
                      //,……
                    });
                    */
                    table.reload('customer-list');
                    layer.msg('已恢复!', {icon: 1, time: 1000}); //消息弹层1秒后消失
                });
                // });
            }
            ,add: function(){
                layer.open({
                    type: 2
                    ,title: '添加客户'
                    ,content: "{:url('Customer/customform')}"
                    ,area: ['420px', '420px']
                    ,btn: ['确定', '取消']
                    ,skin: "layui-layer-lan"
                    ,success:function (layero,index) {
                        // layero.addClass('layui-form')// 添加form标识
                        // layero.find('.layui-layer-btn0').attr('lay-filter','formVerify').attr('lay-submit','');//将按钮变成提交
                        // table.reload('user-back-manage'); //数据刷新
                        //      layer.close(res); //关闭弹层
                        layui.form.render();
                    },
                    yes: function (index, layero) {         //按了弹出层的确定按钮时，这是将在父窗口中获取子窗口form标签里的所有值，并根据name名和值形成键值对json对象
                  
                        // 获取弹出层中的form表单元素
                        var formSubmit=layer.getChildFrame('form', index);
                        // 获取表单中的提交按钮（在我的表单里第一个button按钮就是提交按钮，使用find方法寻找即可）
                        var submited = formSubmit.find('button')[0];
                        // 触发点击事件，会对表单进行验证，验证成功则提交表单，失败则返回错误信息
                        submited.click();
                        // 弹出层关闭的操作在子层的js代码中完成

                        // layer.alert('来到这里了'+index);
                        let body = layer.getChildFrame("body", index);
                        let data = {};
                        body.find("#form-custom-add").serializeArray().forEach(function (item) {    //获取弹出层写下的数据，input，下拉框啊，之类的表单元素（即form-admin-add下的所有数据）
                            console.log(item)
                            data[item.name] = item.value;   //根据表单元素的name属性来获取数据
                            console.log(data);
                        });
                        $.post("{:url('Customer/addUser')}", data, function (result) {
                            if (result === "success") {
                                layer.alert("添加成功");
                            }
                        });
                    }
                });
            }
        }</pre>
<pre class="brush:js; toolbar: true; auto-links: true;">子页面customform.html代码如下：</pre>
<pre class="brush:js; toolbar: true; auto-links: true;">

<pre class="brush:html; toolbar: true; auto-links: true;">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;meta charset="utf-8"&gt;
    &lt;title&gt;客户添加&lt;/title&gt;
    &lt;meta name="renderer" content="webkit"&gt;
    &lt;meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=0"&gt;
    &lt;link rel="stylesheet" href="/public/static/layui/css/layui.css" media="all"&gt;
    &lt;script src="/public/static/js/jquery-3.1.1.min.js"&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;

&lt;form action="" method="post" class="layui-form" id="form-custom-add" name="form-custom-add"&gt;
    &lt;div class="layui-form-item"&gt;
        &lt;label class="layui-form-label"&gt;&lt;span &gt;&lt;font color="red"&gt;*&lt;/font&gt;&lt;/span&gt;客户名称：&lt;/label&gt;
        &lt;div class="layui-input-block"&gt;
            &lt;input  type="text" class="layui-input" lay-filter="Consumername" value="" placeholder="" id="Consumername" name="Consumername"&gt;
        &lt;/div&gt;
    &lt;/div&gt;
    &lt;div class="layui-form-item"&gt;
        &lt;label class="layui-form-label"&gt;&lt;span&gt;&lt;font color="red"&gt;*&lt;/font&gt;&lt;/span&gt;联系人：&lt;/label&gt;
        &lt;div class="layui-input-inline"&gt;
            &lt;input type="text" class="layui-input" lay-filter="Consumerlxr" autocomplete="off" value=""  placeholder="联系人" id="Consumerlxr" name="Consumerlxr"&gt;
        &lt;/div&gt;
    &lt;/div&gt;
    &lt;div class="layui-form-item"&gt;
        &lt;label class="layui-form-label"&gt;&lt;span&gt;&lt;font color="red"&gt;*&lt;/font&gt;&lt;/span&gt;联系电话：&lt;/label&gt;
        &lt;div class="layui-input-inline"&gt;
            &lt;input type="tel" class="layui-input" lay-verify="required|Consumerdia"  autocomplete="off" value=""  placeholder="电话为8位" id="Consumerdia" name="Consumerdia"&gt;
        &lt;/div&gt;
    &lt;/div&gt;
    &lt;div class="layui-form-item"&gt;
        &lt;label class="layui-form-label"&gt;&lt;span &gt;&lt;font color="red"&gt;*&lt;/font&gt;&lt;/span&gt;邮箱：&lt;/label&gt;
        &lt;div class="layui-input-block"&gt;
            &lt;input type="email" class="layui-input" lay-verify="email" placeholder="@" name="email" id="email" value=""&gt;
        &lt;/div&gt;
    &lt;/div&gt;
&lt;!--        &lt;div class="layui-form-item"&gt;--&gt;
&lt;!--            &lt;div class="layui-input-block"&gt;--&gt;
&lt;!--                &lt;input class="layui-btn layui-btn-primary layui-btn-radius disabled" type="button" value="&amp;nbsp;&amp;nbsp;提交&amp;nbsp;&amp;nbsp;" id="submit" &gt;--&gt;
&lt;!--            &lt;/div&gt;--&gt;
&lt;!--        &lt;/div&gt;--&gt;
    &lt;div class="layui-form-item"&gt;
        &lt;div class="layui-input-block"&gt;
            &lt;!-- 隐藏提交按钮，在父层中调用 --&gt;
            &lt;button id="addCustomer" class="layui-btn" lay-filter="formVerify" lay-submit style="display: none"&gt;添加&lt;/button&gt;
        &lt;/div&gt;
    &lt;/div&gt;

&lt;/form&gt;

&lt;script src="/public/static/layui/layui.js"&gt;&lt;/script&gt;
&lt;script&gt;
    layui.config({
        base: '/public/static/' //静态资源所在路径
    }).extend({
        index: 'lib/index' //主入口模块
    }).use(['index', 'form'], function(){
        var  $ = layui.$
            ,form = layui.form ;
        var mobile = /^1[3|4|5|7|8]\d{9}$/,phone = /^0\d{2,3}-?\d{7,8}$/;
        form.verify({
            Consumername: function(value){
                if(value.length &lt; 2){
                    return '客户至少得2个字符啊';
                }
            }, Consumerlxr: function(value){
                if(value.length &lt; 2){
                    return '请输入至少2位的用户名';
                }
            }, Consumerdia:function(value){
            var flag = mobile.test(value) || phone.test(value);
            if(!flag){
                return '请输入正确座机号码或手机号';
            }
        }
            // ,phone: [/^1[3|4|5|7|8]\d{9}$/, '手机必须11位，只能是数字！']
            ,email: [/^[a-z0-9._%-]+@([a-z0-9-]+\.)+[a-z]{2,4}$|^1[3|4|5|7|8]\d{9}$/, '邮箱格式不对']
        });
        // 验证成功后才会执行下面的操作
        form.on('submit(formVerify)',function (data) {
            // 提交成功后返回信息，关闭弹出层
            parent.layer.msg('操作成功',{
                icon:1,
                time: 2000
            });

            //当你在iframe页面关闭自身时
            var index = parent.layer.getFrameIndex(window.name); //先得到当前iframe层的索引
            parent.layer.close(index);
            //使用parent找到父级，重载数据表格
            // parent.layui.table.reload('Customer-list');
            window.parent.location.reload();
            // 刷新表格（即点击分页控件的“确定”按钮）
            // parent.$('.Customer-list').click();
        });

    })
    $(function(){

        //防止用户无更新提交,只有表中数据有变化时才允许提交
        $("form").children().change(function(){
            $("#submit").removeClass('disabled');
        });

        //失去焦点时,检查用户名是否重复
        $("#name").blur(function(){
            $.ajax({
                type: 'GET',
                url: "checkUserName",
                data:{name:$(this).val()},
                dataType: 'json',
                success: function(data){
                    if (data.status == 1) {
                        //  alert(data.message);
                    } else {
                        layer.msg(data.message);
                    }
                }
            });
        });

        //失去焦点时,检查邮箱是否重复
        $("#email").blur(function(){
            $.ajax({
                type: 'GET',
                url: "checkUserEmail",
                data:{email:$(this).val()},
                dataType: 'json',
                success: function(data){
                    if (data.status == 1) {
                        // alert(data.message);
                    } else {
                        layer.msg(data.message);
                    }
                }
            });
        });

    })
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</pre>
<br />
</pre>
<p>
	<br />
</p>
<p>
	<br />
</p>