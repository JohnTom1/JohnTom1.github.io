---
layout: post
cid: 13
title: http响应状态为canceled
slug: 13
date: 2021/02/02 17:58:07
updated: 2023/11/14 15:51:40
status: publish
author: admin
categories: 
  - layui
tags: 
---


在用layui模板弹出层时，将子页面的数据返回到父页面提交到后台时，没有reponse返回值，status为canceled<br />
查阅了一些资料后，把post换为ajax请求方式并且设置async：false<br />
<span style="background-color:#E56600;"></span><span style="color:#4D4D4D;font-family:-apple-system, &quot;font-size:16px;font-variant-ligatures:common-ligatures;white-space:normal;background-color:#E56600;">而至于为什么status = canceled,是由于在提交时，form action与绑定于button上的click事件会同时触发。<br />
form action将表单内容以serach的形式追加至当前url上，<br />
url变更后会导致页面重新加载， 而这正是导致post请求在执行后就被终止的原因。<br />
<pre class="prettyprint lang-js linenums">  //事件
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
      
                    },
                    yes: function (index, layero) {         //按了弹出层的确定按钮时，这是将在父窗口中获取子窗口form标签里的所有值，并根据name名和值形成键值对json对象
                        console.log(layero);
 
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
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$.ajax({
                            type: 'POST',
                            url: "{:url('Customer/addCustomer')}",
                            data:data,
                            dataType: 'json',
                            async: false,
                            success: function(data){
                                if (data.status == 1) {
                                    layer.alert(data.message);
                                } else {
                                    layer.alert(data.message);
                                }
                            }
                        });

                        // table.reload('customer-list'); //数据刷新
                        // layer.close(index);
                        // resetSearch();
                    }
                });
            }
        }</pre>
<pre class="prettyprint lang-js linenums">总的来说就<span style="color:#4D4D4D;font-family:-apple-system, &quot;font-size:16px;font-variant-ligatures:common-ligatures;white-space:normal;background-color:#FFFFFF;">是ajax请求默认是异步的。我把请求改成同步的就行了。设置如下参数：async: false。</span></pre>
</span><span style="display:none;" id="__kindeditor_bookmark_start_3__"><span style="color:#4D4D4D;font-family:-apple-system, &quot;font-size:16px;font-variant-ligatures:common-ligatures;white-space:normal;background-color:#FFFFFF;">而至于为什么status = canceled,是由于在提交时，form action与绑定于button上的click事件会同时触发。form action将表单内容以serach的形式追加至当前url上，url变更后会导致页面重新加载， 而这正是导致post请求在执行后就被终止的原因。</span><span style="color:#4D4D4D;font-family:-apple-system, &quot;font-size:16px;font-variant-ligatures:common-ligatures;white-space:normal;background-color:#FFFFFF;">而至于为什么status = canceled,是由于在提交时，form action与绑定于button上的click事件会同时触发。form action将表单内容以serach的形式追加至当前url上，url变更后会导致页面重新加载， 而这正是导致post请求在执行后就被终止的原因。</span><span style="color:#4D4D4D;font-family:-apple-system, &quot;font-size:16px;font-variant-ligatures:common-ligatures;white-space:normal;background-color:#FFFFFF;">而至于为什么status = canceled,是由于在提交时，form action与绑定于button上的click事件会同时触发。form action将表单内容以serach的形式追加至当前url上，url变更后会导致页面重新加载， 而这正是导致post请求在执行后就被终止的原因。</span><span style="color:#4D4D4D;font-family:-apple-system, &quot;font-size:16px;font-variant-ligatures:common-ligatures;white-space:normal;background-color:#FFFFFF;">而至于为什么status = canceled,是由于在提交时，form action与绑定于button上的click事件会同时触发。form action将表单内容以serach的形式追加至当前url上，url变更后会导致页面重新加载， 而这正是导致post请求在执行后就被终止的原因。</span></span>