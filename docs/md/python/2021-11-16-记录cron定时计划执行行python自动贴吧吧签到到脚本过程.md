---
layout: post
cid: 442
title: 记录cron定时计划执行行python自动贴吧吧签到到脚本过程
slug: 442
date: 2021/11/16 21:32:38
updated: 2023/11/14 15:51:40
status: publish
author: admin
categories: 
  - python
tags: 
---


<p style="margin:10px auto;padding:0px;color:#393939;font-family:&quot;font-size:14px;white-space:normal;background-color:#FAF7EF;">
	apt-get install cron
</p>
<p style="margin:10px auto;padding:0px;color:#393939;font-family:&quot;font-size:14px;white-space:normal;background-color:#FAF7EF;">
	启动cron
</p>
<p style="margin:10px auto;padding:0px;color:#393939;font-family:&quot;font-size:14px;white-space:normal;background-color:#FAF7EF;">
	sudo service cron start<br />
安装：apt-get install cron<br />
（centos:<span style="color:#ABB2BF;font-family:&quot;font-size:14px;font-variant-ligatures:no-common-ligatures;white-space:pre;background-color:#282C34;">yum install vixie-cron <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;yum install crontabs</span>)<br />
启动：service cron start<br />
重启：service cron restart<br />
停止：service cron stop<br />
检查状态：service cron status<br />
查询cron可用的命令：service cron<br />
检查Cronta工具是否安装：crontab -l
</p>
<p style="margin:10px auto;padding:0px;color:#393939;font-family:&quot;font-size:14px;white-space:normal;background-color:#FAF7EF;">
	查看本机上所有cron服务
</p>
<p style="margin:10px auto;padding:0px;color:#393939;font-family:&quot;font-size:14px;white-space:normal;background-color:#FAF7EF;">
	ls -l /etc/init.d<br />
crontab -e 进入vim界面添加任务按照<br />
我的任务参考如下<br />
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA4gAAABJCAYAAAB/7AhCAAAeHElEQVR4Ae2dbY/dxnXHr2w9rK7WXq+80kr7IAfSWrJrFW69cuNYWsdya0lOJMdyWzS1UTl2jABBbbho6qAoggKpEbtG+gEKGMiLAAEKo98iaGD0awQJ8i0mOHP5J88Mh+RwLsm9D/8XC969l/NwzvnNmXM45HC0srNq+EcdkAEyQAbIABkgA2SADJABMkAGyMCIEBACMkAGyAAZIANkgAyQATJABsgAGRAGmCByBZUryGSADJABMkAGyAAZIANkgAyQAcsAE0SCQGdABsgAGSADZIAMkAEyQAbIABmwDDBBJAh0BmSADJABMkAGyAAZIANkgAyQAcsAE0SCQGdABsgAGSADZIAMkAEyQAbIABmwDDBBJAh0BmSADJABMkAGyAAZIANkgAyQAcsAE0SCQGdABsgAGSADZIAMkAEyQAbIABmwDCx8gnjqqTPm/18/Z373l2vm69un5gf83TXz8ztb5g93N8xPL56cn34vy8CifcjkkKyTN/I2JG9si7yRATJABpaaASaIszoAGBDO9sCkfWbbPrM6rlP7Rd7IWyo7LEd2yAAZIANkoCUD1QnihcfN/75+zvx6f5wr9eVvnDd/uLdpfvknJ/LvZv2FmlxB5As/e2GUAfvc+IBe7N/S0U7dB/JG3oZmju2ROTJABsjA0jJQmSAisdIJ4g9ubjNBHGqwMCCc7UFJ+8y2fYYap0O1Q97I21CssR2yRgbIABlYegbaJ4hz9kwcEl0+g8iVxKlXcbTDZMC+9M6zU540W6HP5I28hbjgd+SCDJABMkAGemCgMkF89M/PuauFCFC+vW7e3ipuO00KkrLbV397fdWsXHjcfHl7cuvqb248ZjeSOfizTbuxjGzQMu3trH6C+PILZyd139u0G8D8St1CmyRLF0bZXTPvf32ymY7cwit/v3/1jD1WbVJz6spp8/k3J+eizFevnjYP9h5xB8pQup6ynWh5dlYNbGr58XV3d8P8ev+Rbjck8tvo0D6xq/IYj1bmLpgbqA7YVTaK0px+cjV8wQLn41w5dsb1NIzurpmDZzfMl7fO5nKgbyFZpmI0gbdD810DcUT5wuOFeqFeyAAZIANkoA8G3AQRSWCWpOggLfQ5OVjNArXf/dXpPDlE/b96fr1I4KQfUyakCNRkBfHzl7ec4A5t6tto+1BybZ2ZLtCX0jGwYivJgg64/TKOPEPpeop2WsmjE8Qb2U6vAV6T2fQD3p7tg+d6HZv5fdhZNbHn1bIWqLfP82vtGhjXteff23Seh5YLS/KMdCsfklIm0xn07481/O/bD37nt20ZTeCtTxuybgYeZIAMkAEyQAaWj4FDTRBtcJUlQDoAk2Tuhd3TNgCsWkGLhRWBGgK5/7uxmq8u5W0GgtXY+qc6TyXkIvODS8XrLK5fXp8kz36CqAJILcvK7pr5wcvZKo0uo86HLnO5723a1390ouvUdlS5KHlUgti7TQewjyRFIoefYPhcxa40+uUO63897uTOAJ/t/3zJuxOhLQfq/GiuU8ogQXzhrLFy6BV6GXPZc9n+hSwtv9hXs52PP9/vpPA2cNJ/WDyx3eULTmhz2pwMkAEycHgMuAmiCjZsEBNINDp5lk8FaljpQaCMYE8Sni7eA6gDNbSVA4d+aDmVDvLzevoOMgd1WiE/gsuSLFkfEbDmCQdkvLdpUAbtdqrrxHZay+MliJAptxX60YFNoac+7QM+tRxoV99ebe3agUy5nnpiGvWDQy0XfgsdW3MAO7fhOqVMk55Qp2cb2FWSw5IOKsrA7m14C+mS3x3ehErdU/dkgAyQATKwCAxUJog2wFNXuBHwlIKdpgAq9HsgQEJwlNdfkSC1VTr6PYtBF4LiPJnTugrJj+9qXjUCPebyDqXrlHZS5FEJYi5jk9707y0+D2kfLUspuYKe1HhsOw4GPT/AQm37kK9vrgP9wnhJ9jvoe0WCqO2a66CiTGveWrCct80y7jPa1Af1QQbIABkgA2SgxEA4QUQAowJSBFLBZKatYhGoBepPDtQq+jDLCSISAb1SlAdysIEOPKE3/Z0nd0lelOlb1yntoEwbeQZMEAexD+wM+2Q6+Uo2KfK+CyYbnv1zfg7x+xKDTX1J4QBloKOdVQMfVelDUsqovsvmWdYugWde89X47PxaHcDmHveteVN9mwW7sw+8ak4GyAAZIANkYDEYcBJEXMHGs121RxWYtYZhykCtTXspgVqb+qc5t3VACL15gaXuQ0lelFH2agykUwLPlHZQpo08C54gWtvc3TCf/OlpuxGRvXiQ6SlPfFLsM2CZEoNNbadwgDJtuE4pk/UdY7XSJ3oM1+qACWLpSqX2Yfy8GMEF7Ug7kgEyQAbmlwEmiHe27Osufnqx2CBmKKARdAZXZRHM6sCzIrDU/S0lf6inTSDdFNCHfk9pJ0WeQ0gQe7XPzupko5PMzsKErBRi4yBJCpFszEuCiB1G8xXQEC/6uxQOUnhLKaNWJiU5/OUzp9zkpqLvsFlw1beiTGt/oHXIz65dqA/qgwyQATJABshAMgNOgohEA8GNDkgRvARvh2xrgMRADf1rc4QsbQK1NvVPcy5WbLWebX0IIOVWNp0gIpkIbXwhNlDl8qRmKF0ntgOuSjqokmfABHEQ+6hXWEjyIRszwXZWN99eN+9c3rCrifh+GuYGKRvisMFHtOYghbeUMso+QR+C97h64zTF76TwNog9G2zHPszvFWLajrYjA2SADJCBEAPtEkQvCApVGPVdYqAWVbcXzKQEaintpJRB3/TKhLwo3O7eiuecPJ3rMnrrfOc1F2q1MLSaU1plREDvtdVKpkSbtpZnwARR9w0rR53bR61Q/ebgceeCAOz0Py89bl+F0cnFGW98tLJxi7JIdoRth9OdVSOvcPFfc6F17ZyvX98yLdeJjMIOzsWa3TUjzyTm7yP1xg7kCSaVFeMNZdr4g77sx3oZMJABMkAGyAAZWF4GggkiAqJ8xQIBjQ7QWgSLJcASA7VSPRF9QNDVJlBLaSe1DFZOJCjUf6J7+5sXeEo7OvjWZexn//yhdD1FO63kGTBBFF33bh8lj9jP4RQ6Dawkp/I2ZLn8vZwe25bTgC9pxQF0o+qB38pXo+G3MCZSyoiPQbmQHHc3zFe3zjmJveg41e+k8DakTdnW8gYLtD1tTwbIABlYHgaCCSICtTxBRICkgrGpIAnU1xjcRSSDoT6lBmqhunr5bnfNvP/C+Xwl4vevnsmfc6pKEKUfB89umC9vnS2Syrsbkxd5X/KepRxK11O2Ey3PFMF3kv36to+XgORjLuM9Txi6GnuJ4yhJdyFO78lOoKfNJ1fDTjaagxTeUspk+pKVY3+8yUrni3vhCznJfieRt1T7sFyYQ+qFeiEDZIAMkIFlZiCYIC6zQig7HQIZIANkgAyQATJABsgAGSADy8oAE8SBV1SWFTTKTSdLBsgAGSADZIAMkAEyQAZmnwEmiEwQk7fA5QCf/QFOG9FGZIAMkAEyQAbIABkgA20YYILIBJEJIhkgA2SADJABMkAGyAAZIANkwDLABJEg0BmQATJABsgAGSADZIAMkAEyQAYsA0wQCQKdARkgA2SADJABMkAGyAAZIANkwDLABJEg0BmQATJABsgAGSADZIAMkAEyQAYsA0wQCQKdARkgA2SADJABMkAGyAAZIANkwDLABJEg0BmQATJABsgAGSADZIAMkAEyQAYsA0wQCQKdARkgA2SADJABMkAGyAAZIANkwDLABJEg0BmQATJABsgAGSADZIAMkAEyQAYsA0wQZwiEtf2HzPaDkVl9+tTSDtDVqw+Zf78zMrf2xguhgxNbT5ifHbto7m8uhjxtXrLa3blj8+79kfnFWyPzt1dOLgAXyyHPqaeOmZ+/NTJfvDkyT24P59O+dXvCyqe3U9udf/tMr4PwC6UPy6bd+RJXrqHkGaodX0/Tc8Cx4OsU/x+WTdF+0xG2l3kz/3t7ZA4G9MVNfWz7u+j84ywWEJm+uD8yN59ibNVWj7HnM0GcoQRR4F/2BHG8d9x89NriJIgrO9vmR8eZIMY6pNB5sz4Rh/pc992yyHMYcqJNBERpFxRmJSgem9sHI/Nfb7e7MNKNDtxECjyj7qGTfrTf9XEoeYZqR+sHbXIsFAlSmj+Yz7GwaAmizzO4lmOXdtVjaNk/d5ggjs039o+YD18e2RUgWQX6yc2R+eD6UfO1nearx3tXj5p3XhmZj+4U5f/t+sPdrRZsnzXvrl40Pzt+efJ37KL58aPnzY3Nhr5tnzXfWc/K9bASdOa1kVl7fsXKKQNAEsQJlGNz+qUj5sy3jnWngxlKhvXAu359ZL77zAkrpySI//TayDxnr3JNmBKG9Pmz/vnF9Uvm/Y21rM/b5kfHLkyu2u2um+sbF8zHj2zMlTyHre9nDyYT/Af7k3Fy2P2Ztv1lkQcT+tDJBAKjuV9B3F4x/5pd/W8bAE2vg/kMituOzaEYHaodX/7pOZiRiyUcC1PFDODvF3O7glhw+N+3H8ruSHG/89nn/2Ef3kYvnSWI118sEjtJDp2/POAvd3i8d8I8uOmdn5XvKkF88vwT5l9OZIkhEkQcj14oJ4m760bKfPyIV6bzBHFsJEHc+oeROfc3I7N2bZIgnnrqhDn315PvFz9BHJu7GTtyQeEvnjlqE8Rrl47nXMReZGgDfm/n7q7nFxQ+G++aG5tbkwRx64x5L+NJEsQhb7nrTdYhLjggMJjbic3zeUskD4KSoRPE6XkvAo+2idn0bStewMoMXSGfX5sqvSq/NZQ8Q7XTKX9WTxwLVTqdJ5uir3ObIMIXenGAPJYlK4jzN8eE/VEVa4f1fXcJ4vWReXv/mLNaKKuCWBH84bXj5Ssg2yvme1kyKMnBnasnnPKdKGX7rPneiSv2ObDvrxeB+d65rTxp/GzVXdGxz41lCaQE+QdbZ/I6+niW7NRTJ/NEUZJFWUVc/MTQHSDjJ08aWUnUFxbmKjFUQYdwe2Jr3chKol6xZmLo2jxmfGMC+ORgMVbSl0keBCXzN3kzKK4am/Nr07DvSZdnbN57c2Ri72pIbyfc7yr7dP89x0KVTufJpujroiaIsqpYZSd+n+5DOksQq4xwZX8S9IdWA7Hq2PcthJfOPGG+/3j5QdY8ETya3QKYBfknL5w17566YN4485iFTv5HktlHgriyU6wkIkE8/c1AQu0lIVU6n8/vxzZBxAUFSRT9Cw5zJdfuJEHMV66PXTT6AsVcyXJo3NUHJ5j0wglIfVkZc3L7lWyigmcZvnhjZD54LjzucKvWZEXJLSsPysetNDX1CY7crd9eIe2pb3K3wgNPD5/fH5m/3w/rweW2Xh7fPlefO+Lo+9P8ViHIjePYXN0/6mxGIDqo6xfsA1vao3e12e170ZY85+dzgHq0XX153PrqdeGei7bLR1xAQPt1Rz85mUYH/lgQXYc2f/B10KdNY3VWPi9+/PjyPHvgMvpRxYUpudsHzMRcvPLb6VNv03DAsVBmZ77HwsTHgL+YBBFzgvY9VgdXqh/xkDJ68xhdFp+1Ly2P2bIvdM8p/Kv2e2A9Zgy69TW1x99FX4MliKUVRKwe1tx+2rdBqxJEv93+EsQiMdS3mMrkI7eYLsdKYvgW0zvPHF2oW0zvb56f3GJ67KJ9BpG3mDY7YExq4QRw1dT/XkwopYkJt6uo5BCTmBxL5++s2mTS/nbZ3UWtqZz2JfX9zfQxYN8kGUGQq+WwnyOSqyZ59O8PbhWJuG4rdOUXz2jq8/TnUDCAQEGf1xgMNeha6tIsaHnK47eGtxYXWAZPEBt0oOUXlrUO+rapHjvRn3uQJ8Sb1oVwUn2xYzKuh9Qbx0Lhr7v0B3M3FpTfAX9NPrF2TnhrZEJjoakMbODrL3pMZ3JgXpB44Okrx/Odzavig7b18/xyTNZrgrj3zEP2FtOfvHKkdOsoXmcQWlkcylBIED89eb72mbD+EsRVe2spN6nhJjVDMT9P7SDQ0VcMdf8x6YUniOqAHRNN8bD7xDHKpPPObTcpQHvoCya7T2483PpBedRRJY+0NVTfoLtJcOuuFlk93DnSuB16kzy6DbTzdLYluaygQJd+4CCrOLLBzE3nivXkyr4t05C85u3WnlfwIfzo1TKRH1fDdd9Qb1vewFDro0p2dD9i6kFf6wPCQgfuWCh07cua15tdXBE7DWHTGJnlnLbjpywPNsAo6qrToV458XWl+1xuZxi95e1yLJg6O8odJXiV0qKMhSB/dRwof+Ne8Cj8gfhf1xeF9SbjQutT9yX5s+of5o66MZfcjkqsl72OThNE+4oCb4Oaf7z+UCk5FKXj1tMf7h8t7X4qtxf2/vzZ7rp5/dEr9hmxHz+GHSfLGbT0tc8EUQMozpyvueBrLjQTS/sZk0HNhIbgJzxJFBOXO6EVV5frEjVf70iGZGLyb0PFqk+4H5lPiZBH2kQ7ffcN7YRW8HzZg/9HyAP7iM5CV57Rh9BvtW2WghTXb+ft1rBTb7MwO6g3bOdwmaAcsQEIdNwgb6gN9LUuKMY5TfJoFlFmaJuGZAx9B6Z0n0Pn4TstT2ksROu/sH3Ve9l0OyHe0e/Qb+irc4zsW94ux0Jtggg9LdJY0LxAvjp/oC+u6LL4HGK0rt6631Bnm6NOOqv8T5v6eK47b4b00XuCKMmebEAzeW1B0SEkiHpTEv9zaOUxJETKd3tnsw1EvOcPQ3UNlSBK0LLsCSJWlm/tlZ8ZDdlm1r+zq9Sd735bjKNZlz+1fwjg6wImTEBNk7qfIGIiRLJXvl2wrN/Q5AjZ6vsxqStGHqlvkL5FBpeQL3SMkadJL6ijFJhXJlBFIO7bVPcR7cYEQ2G+wu2g3ra86b61+jyFndDXdB0ULGodod6wDlZNXzaN1Vvb8VMvT5iDqr7AR4hf8fmsb6c/vaHddA7COkC9YQ7CZar0FvU9x8JUm7DAXtUcFDaruriCsa1tXldv3W9RNlfzQF5X9iy6jDE9zvC77lvbNnh+Oe7pNEH0FXxRvcLCT/awQY0khbIZycUni/cRNu5+qsDx24z5X15hYXeXjAzch0oQY/rOc8oQUyeLppNisvIDLW3r+kmhvg4dzMlEI1f+6zZmwflVk6fuV/lzfV/889EWJsGu+1avtxiW4uRpagcBRyhBlFtQZWME6MA/xnBRHQw1rdSG5auXJ1zGt22r/3sOin3OfB3j/64SxGls2kZvvlx146drm+q2NaP17dQniNPoDe1yLIxqVxC13cB96DhvYwHjppGDCF+DOtwkrPB74sdxsVWv9oX8O/oVdyzagP5hL/Slbi6JayNm3lu+c3pNEK1hsBnNnZH57tWT+VUQrCCWNq/Jkj/83vUzivnKYWRyKDIwQVy+gUGncng2x0TUNLHgPEwSrs2KSUUHavocmcT8HTyrbhHDhJSSIKKfTfIM1Tf0J6y3ZrujfJM8OK+qnapJHboOBWj4rsqmokO0y6B4doLiaW2qx0bM59ixDVbCjDb7EN0XvXrp81nfTnWCOK3e0C7HwvKOhSifmJwgFuzCNzvHmlub9dip+wyGnTGq+ivzEMYJEsi6+vhb8xwPHfWfIO6sGqwWtkkQcathlwliSnIoimKCGA8UwOKROktlAM6+KRkLThz53QXtgju9MYkzEWX1xfYpJPM0ZaW+zvuGyTVx8o6Vp94+xS2MOtFE0ihBhv+sp95Iwg/Atd7RbkxQHAwooB/vVkHUG+Ijtm+6n42fK/rRWC4ySUZCE9RBPo5cP1avg/5sGiNz1Tl146denlgfUpxXdYGpvp3+9IZ2ORbqE8RFHwvNHBQMV/lW+Gbtr1eUj/pnb6dq2egGG1hVjc2Y74Ptah+ndiNvihli2uM5hc/vP0FUK4j6uTJsaOPfegrjdL2CmJocSn+YIBbAwD48UidxDBQTj0wYjWUw4UQkL3WTHiZ8STSqJjy/L3X1xSZFfp35BBohT6msCtK77VthkzbJge1fgn2aEio9qcNuwTLbK8HdRX291ekK56IdJ9ix+i5047NTVy/q88ugvaQjdN2CYbRT11ecUxV44ffQEfUG7aN2guzWpoVNonyIGjeQAf32EyV83yRPpQ9RTIbrmMwTse10q7e41XSwy7EwMmUdVM/zh2PTtLGAvvr8Y3zIEXNcWAdFu3rOgA/R3+k6u/iMNkLjC7+J3w393kX7y1xHrwmifgaxvBI4Nq/fHBl5BtHdsXRsrlw7Yr+X33RSmWqoF9eLDWlubBbPOsbWxwSx2knG6pDnLacOEXyIA5c/HQCFmIDDj5pwVACtXzuBiQ5tusHd2N5W+tHBw97VzbG5fWPSx9BEgzqb+u/L1EqeneH6pu3ibmk+WbF8p+I1F23kQVBiV1XUKyv08ym+rlG/2K6w29jIc1j6nY3Fb+VxhXbrgqH8HLVSqfsVZCeJt3L/fEaq/y+CMtGTfhVHdZlJe7l8dRcmlDz2tSLZK0gmdY/N1f2j5uM3R87rTlDvkDbVrNb7kPbjJ5fnzVH+/FSh20L/Id5QVvrkj6GiDtceQ+pN+pD3sYaD/ByOBTtHLcZYcP1ObuNIDlye1WsuvPIYm9Y/XVnx5lS3D/6YiP5f+SlJXvVzjvKICHx1nb+PbitwcWmZy3aTIKpVQn8nUvm/apUQq4ihMvJd1fOJbQyGdx3aTWmOX55sThM46nch5glh4Dxdz2erG80rIgSOOlpiBjCBwInXJ1j1AVlo3Pv1ox2ZsPAibze4K9rAuf4x1Me0BLFoy+1D1cRZnO/3Cf9317fiijHqdo5eIDDRfdG/GHnyoETdAuS04SSBmU5UMOCfK/9//sYkIHDabyiDevyLDrApfsdRzsNvTjveLrM4X47VvFXZOu57nTDr9uSzw0KiDhpt5HHQeH5XNlU+0x/jjtzqPH2br68r/O+XhTxiPwSehZ+p5n3t2rH8goXPVVG+sDHaQT9CR5+1/O6DivHDsVAkB45dORZMEzvgz2fXH2s4D0ef0Riu5WJseWwVYyM0XvzvmvqFsRAex+3a8tte5v97TRA/fGVkru2t1CYI470T5p1XJiuJSBQn5bp5zQETRA6OZR7ghy97EWQ13R6GySZ8i0sVx5OVP726hAmpKsgPbWAhE2D5ynHRJupyAhEnOC3Ohc5T5Bmqb+ijXSXydguV3UNDO7q2lydbhbo/yoNpBBruFWpXd6IDvKheny/Ps8AOTqCSGBBKQiGrxmDnizeK5x6D7Vh7u2Wkf028Qdepx5CNpF2HxWQdyCpTebMmqT88HgayqTO22viQNrIUK2zhwLJo1+Et4+C9Nz0bOH12mRbWYEfwptmuCqA5Flw9QofQHY4cC66eUhNE8VEhHYd9waRN+EqxRdXO0+3mdE+WbFzV9Qtzk/Shi7ZSffWilesmQax1jGFjL5oiKQ/tTAamYwATjTPZz7FvoTzT8cDxRP2RATJABmaXAazshS+wyOZLR/JbQMsXWWZXLjI3sQ0TxDkOQAkxHczCMIAVEO+WtrmVj/LU3jkyt3blfEG7kgEyQAaMvqW76qKuXtljgjh/8SoTRA50OnsycOgM4Eqk/0zEvCYSlGf+JsN5ZY39JmtkgAwMz0BxC7a/+ZL0pe71MsP3lXyk6JwJIpODQ08OUsBlGTo8MkAGZpYBrCBXbDCCZ6f8I6+yk+mZZTo1VuJYWNgYq24TLe3b6Nfm068xQUx1eiy3sE5v4SZoskpWycCwDDAoHlbf5Ht29c2xMLu26WDcVG1yJZt+YQMvxlRMEBd6EBDw+QScdqPdyAAZIANkgAyQATJABshAPANcQezgCgqBiweOuqKuyAAZIANkgAyQATJABsjA7DLABJEJIld+yQAZIANkgAyQATJABsgAGSADlgEmiASBzoAMkAEyQAbIABkgA2SADJABMmAZYIJIEOgMyAAZIANkgAyQATJABsgAGSADlgEmiASBzoAMkAEyQAbIABkgA2SADJABMmAZYIJIEOgMyAAZIANkgAyQATJABsgAGSADlgEmiASBzoAMkAEyQAbIABkgA2SADJABMmAZYIJIEOgMyAAZIANkgAyQATJABsgAGSADlgEmiASBzoAMkAEyQAbIABkgA2SADJABMmAZYIJIEOgMyAAZIANkgAyQATJABsgAGSADlgEmiASBzoAMkAEyQAbIABkgA2SADJABMmAZYIJIEOgMyAAZIANkgAyQATJABsgAGSADlgEmiASBzoAMkAEyQAbIABkgA2SADJABMmAZKCWIJy+cNS/ded78x9+9aP8+vLltvrZzisAQGDJABsgAGSADZIAMkAEyQAbIwIIz8EfKKPtnzh2jfwAAAABJRU5ErkJggg==" alt="" /><br />
/usr/src/baidu_tieba.sh中的脚本内容比较简单
</p>
<pre class="prettyprint lang-js linenums">#!/bin/bash
cd /usr/src/
python -u baidu_tieba.py</pre>
<p>
	<br />
</p>
<p style="margin:10px auto;padding:0px;line-height:1.5;font-size:13px;font-family:&quot;white-space:normal;background-color:#FFFFFF;">
	#! /bin/sh
</p>
<p style="margin:10px auto;padding:0px;line-height:1.5;font-size:13px;font-family:&quot;white-space:normal;background-color:#FFFFFF;">
	符号#!用来告诉系统它后面的参数是用来执行该文件的程序。在这个例子中我们使用/bin/sh来执行程序。
</p>
<p style="margin:10px auto;padding:0px;line-height:1.5;font-size:13px;font-family:&quot;white-space:normal;background-color:#FFFFFF;">
	当编辑好脚本时，要想执行脚本，必须使脚本可以执行
</p>
<p style="margin:10px auto;padding:0px;line-height:1.5;font-size:13px;font-family:&quot;white-space:normal;background-color:#FFFFFF;">
	下面的命令，可以使脚本可以执行
</p>
<p style="margin:10px auto;padding:0px;line-height:1.5;font-size:13px;font-family:&quot;white-space:normal;background-color:#FFFFFF;">
	chmod +x filename
</p>
<p style="margin:10px auto;padding:0px;line-height:1.5;font-size:13px;font-family:&quot;white-space:normal;background-color:#FFFFFF;">
	然后可以输入./filename来执行脚本。
</p>
<br />
python自动贴吧签到可以各大论坛找<br />
我找的
<pre class="prettyprint lang-py linenums"># -*- coding:utf-8 -*-
import requests,datetime,re,os,sys,time
from bs4 import BeautifulSoup


'''
    函数match_bar_name用来获取
    1、当前页
    2、关注贴吧名字和链接，返回列表数据，格式[{'name':'abc','link':'www.asdfaf.asdfasdf'},'name':'abc','link':'www.asdfaf.asdfasdf'}]，
'''
def match_bar_name(soup):
    list=[]
    for i in soup.find_all('a'):
        if i.has_attr('href') and not i.has_attr('class') and i.has_attr('title'):
            if i.string != 'lua':
                list.append({'name':i.string,'link':'http://tieba.baidu.com/'+i.get('href')+'&amp;fr=home'})
    return list


'''
    函数get_bar_link用来获取
    1、所有页
    2、关注贴吧
    3、名字和链接
'''
def get_bar_link():#遍历所有页，直到最后一页
    url=r'http://tieba.baidu.com/f/like/mylike?pn=%d'
    pg=1
    tieba_list = []
    while 1:
        res=s.get(url%pg,headers=headers)
        soup=BeautifulSoup(res.text,'html.parser')
        tieba_list.extend(match_bar_name(soup))
        if '下一页' in str(soup):
            pg+=1
        else:
            return tieba_list

'''
    name: 贴吧名字
    link：贴吧链接
'''
def check(name,link):#获取每个关注贴吧 提交数据tbs，然后签到，并返回签到结果
    try:
        res=s.post(link)
        tbs=re.compile('\'tbs\': "(.*?)"')
        find_tbs=re.findall(tbs,res.text)
        if not find_tbs:   #　没有查找到tbs,跳过这个吧的签到
            return -2
        data={
            'ie':'utf-8',
            'kw':name,
            'tbs':find_tbs[0],
        }
        url='http://tieba.baidu.com/sign/add'
        res=s.post(url,data=data,headers=headers)          ######## 签到 post
        # print(datetime.datetime.now(),'    ',name,'   ',res.json())
        return int(res.json()['no'])   #########返回提交结果
    except:
        return -1

def SignIn(data):
    try:
        res=check(data['name'], data['link'])
        if res==0:
            print( data['name'] +'吧签到成功\n')
            return True
        elif res==1101:
            print(  data['name'] +'吧已经签过\n')
            return True
        elif res==1102:
            print( data['name'] + '吧，签到太快，重新签到本吧\n')
            time.sleep(10)
            return False
        else:
            print(res)
            print('未知返回值，重新签到'+ data['name']+'吧')
            return False
    except :
        print('未知报错 重新签到'+ data['name']+'吧')
        return False

if __name__ == "__main__":
    s=requests.session()
    cookie=''
    #自行填充百度贴吧的cookies，浏览器-F12-网络-F5-request-cookies

    headers={
        'Cookie':cookie,
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }

    for i in get_bar_link():#根据签到的返回值处理结果,利用count做最多三次异常重复签到
        flag = False
        count = 0
        while flag == False:
            flag = SignIn(i)
            time.sleep(2)   #控制签到速度
            count = count + 1
            if count &gt;= 3:
                print(i['name']+'吧异常，无法签到，已经跳过')
                break
</pre>
我是放在docker的Python环境中的，需要sftp上传本机再复制到docker环境中<br />
需要用到<br />
<pre class="prettyprint lang-js linenums">docker  cp  /usr/src/  [容器ID]:/usr/src  复制命令
docker  exec -it  [容器ID]   bash            进入容器命令</pre>
<br />
参考链接：<a href="https://blog.csdn.net/wy_97/article/details/86657328?ops_request_misc=&request_id=&biz_id=102&utm_term=%E8%87%AA%E5%8A%A8%E7%99%BE%E5%BA%A6%E8%B4%B4%E5%90%A7%E7%AD%BE%E5%88%B0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-86657328.first_rank_v2_pc_rank_v29&spm=1018.2226.3001.4187" target="_blank">https://blog.csdn.net/wy_97/article/details/86657328?ops_request_misc=&amp;request_id=&amp;biz_id=102&amp;utm_term=%E8%87%AA%E5%8A%A8%E7%99%BE%E5%BA%A6%E8%B4%B4%E5%90%A7%E7%AD%BE%E5%88%B0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-86657328.first_rank_v2_pc_rank_v29&amp;spm=1018.2226.3001.4187</a>