---
layout: post
cid: 10
title: layui弹窗间的传值（layui弹出层传值）(窗口传值)
slug: 10
date: 2021/01/31 22:47:01
updated: 2023/11/14 15:51:40
status: publish
author: 
categories: 
  - layui
tags: 
---


<span style="box-sizing:border-box;outline:0px;font-weight:700;overflow-wrap:break-word;color:#4D4D4D;font-family:-apple-system, &quot;font-size:16px;font-variant-ligatures:common-ligatures;white-space:normal;background-color:#FFFFFF;"><span><strong>主要有两部分</strong></span><br style="box-sizing:border-box;outline:0px;overflow-wrap:break-word;" />
<span style="background-color:#FF9900;"><strong><span style="background-color:#000000;">1</span></strong>、从主窗口传值到弹出层</span><br style="box-sizing:border-box;outline:0px;overflow-wrap:break-word;" />
<span style="background-color:#FF9900;">2、从弹出层传值到主窗口<br />
<span style="background-color:#FFFFFF;"><strong></strong></span><br />
layui监听表格工具栏按钮，然后<br />
<span style="color:#4D4D4D;font-family:-apple-system, &quot;font-size:16px;font-variant-ligatures:common-ligatures;white-space:normal;background-color:#FFFFFF;">按钮点击后调用这个函数然后弹出弹出层，加载editform.html界面</span><br style="box-sizing:border-box;outline:0px;overflow-wrap:break-word;color:#4D4D4D;font-family:-apple-system, &quot;font-size:16px;font-variant-ligatures:common-ligatures;white-space:normal;background-color:#FFFFFF;" />
<span style="color:#4D4D4D;font-family:-apple-system, &quot;font-size:16px;font-variant-ligatures:common-ligatures;white-space:normal;background-color:#FFFFFF;">然后success提前加载editform的form数据（从主窗口传值到弹出层）<br />
</span>
<pre class="brush:js; toolbar: true; auto-links: true;">  table.on("tool(user-back-manage)", function (e) {
      var data=e.data;
      if ("del" === e.event)
                layer.confirm('确定删除此管理员吗？', function () {
                  $.get("{:url('user/deleteUser')}",{id:data.id});
                  table.reload('user-back-manage');
                  layer.msg('已删除!', {icon: 1, time: 1000}); //消息弹层1秒后消失
                });
      else if ("edit" === e.event) {
        layer.open({
          type: 2,
          title: "编辑管理员",
          content: "{:url('user/editform')}",
          area: ["420px", "420px"],
           btn: ["确定", "取消"],
          skin: "layui-layer-molv",
          success: function(layero, index){
          var body = layer.getChildFrame('body', index);
          var iframeWin = window[layero.find('iframe')[0]['name']];
          //得到iframe页的窗口对象，执行iframe页的方法：iframeWin.method();
          console.log(body.html()) //得到iframe页的body内容
          body.find('#name').val(data.name);
          body.find('#email').val(data.email);
          body.find('.layui-hide').val(data.id);
          },
          yes: function (index, layero) {         //按了弹出层的确定按钮时，这是将在父窗口中获取子窗口form标签里的所有值，并根据name名和值形成键值对json对象
            //console.log(layero);
            // layer.alert('来到这里了'+index);
            let body = layer.getChildFrame("body", index);
            let data = {};
            body.find("#form-admin-edit").serializeArray().forEach(function (item) {    //获取弹出层写下的数据，input，下拉框啊，之类的表单元素（即form-admin-add下的所有数据）
              console.log(item)
              data[item.name] = item.value;   //根据表单元素的name属性来获取数据
              console.log(data);
            });
            $.post("{:url('user/editUser')}", data, function (result) {
              if (result === "success") {
                layer.alert("编辑成功");
              }
            });
            table.reload('user-back-manage'); //数据刷新
            layer.close(index);
          }
        })

      }

    })</pre>
</span></span>