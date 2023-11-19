---
layout: post
cid: 8
title: tp5返回数组variable type error ：%s
slug: 8
date: 2021/01/25 15:59:02
updated: 2023/11/14 15:51:40
status: publish
author: admin
categories: 
  - tp5
tags: 
---


<span style="color:#333333;font-family:&quot;font-size:14px;white-space:normal;background-color:#FFFFFF;">修改该异常方法，将是数组的返回进行json_encode</span><br />
<pre class="brush:php; toolbar: true; auto-links: true;">/**
 * 获取输出数据
 * @access public
 * @return mixed
 */
public function getContent()
{
    if (null == $this-&gt;content) {
        $content = $this-&gt;output($this-&gt;data);
        if(is_array($content)) $content = json_encode($content);//修改语句
        if (null !== $content &amp;&amp; !is_string($content) &amp;&amp; !is_numeric($content) &amp;&amp; !is_callable([
            $content,
            '__toString',
        ])
        ) {
            throw new \InvalidArgumentException(sprintf('variable type error： %s', gettype($content)));
        }

        $this-&gt;content = (string) $content;
    }

    return $this-&gt;content;
}</pre>