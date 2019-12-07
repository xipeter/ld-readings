# gitbook
这是一个用来写“书”的工具，然后变相的，也可以用来写博客啦；

# 安装
可以参考[gitbook官方入门](https://github.com/GitbookIO/gitbook/blob/master/docs/setup.md)。主要是安装nodejs的时候需要注意：12.x版本的nodejs可以直接在官网下载二进制包，也已经自带npm，apt-get或者yum的反而有可能因为源里面的版本太老安装之后无法正常使用。

# 用法
* 用markdown书写，git管理版本，gitbook-cli做服务，也可以部署到gitbook.com上面；
* 根目录下面的SUMMARY.md是入口，在这里定义整本书的结构，可以参考[chapters](http://caibaojian.com/gitbook/format/chapters.html)
* 支持一些类似jinja的语法，可以参考[templating](http://caibaojian.com/gitbook/format/templating.html)和[conrefs](http://caibaojian.com/gitbook/format/conrefs.html)
* 所有的配置都以JSON格式存储在名为 book.json 的文件中，可以参考[configuration](http://caibaojian.com/gitbook/format/configuration.html)
* 如果需要写数学公式的话，要装插件，详见[math](http://caibaojian.com/gitbook/format/math.html)

# 参考资料
* [gitbook的代码仓库](https://github.com/GitbookIO/gitbook)
* [gitbook官方入门](https://github.com/GitbookIO/gitbook/blob/master/docs/setup.md)
* [一个不错的中文文档](http://caibaojian.com/gitbook/)

