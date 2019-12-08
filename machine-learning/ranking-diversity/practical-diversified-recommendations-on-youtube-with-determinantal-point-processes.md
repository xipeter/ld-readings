# practical diversified recommendations on youtube with determinantal point processes
[pdf](https://jgillenw.com/cikm2018.pdf)

## logs
* [ 2019-12-08 17:35:05 ] hold
* [ 2019-12-08 16:24:17 ] begin

## tags
Google CIKM 2018
DPP


## Highlights
1. 处理多样性问题，在启发式方法后，进阶办法是走形式化的模型，本文使用DPP；
1. 用session长停留来衡量用户满意度，简单的根据相似度卡阈值或者降权，-0.05% ~ -0.41%之间，DPP +0.63%，Deep-DPP + 1.72%；
1. 

## Problem
1. 在线推荐系统很容易出现重复，因为相同主题的item容易得到相同的质量分、点击率；
1. 多样性有两个角度的效用：提高宝贵的推荐机会的利用率，以及为用户和模型提供探索空间；
1. 即使拥有一个可以对推荐集合打分的模型，直接set-wise或者list-wise的打分会面对排列组合爆炸，代价太大；
1. DPP可以直接对一整个list打分，不用逐一的打；


## Related work
1. 多样性的效用之探索：帮助用户发现新兴趣，尽量把topic、子topic都覆盖全；以及帮助推荐系统进一步了解用户，提高为止领域的权重；
1. 多样性的效用之提效：降低推荐list的冗余度，把一些打分低的item提上来；所以一个重要的启发式方法就是软去重，有bagging的方法，有MMR方法，有submodular optimization方法;
1. 以电商为例，重复可以进一步分解为：替代品，可以互相代替的，一般在加购物车后推荐；辅助品，共同满足需求，一般在付费后推荐；
1. 这些方法都不是自适应的；
1. Youtube最早的办法是rule-based的，例如一个作者不能给一个用户的feed贡献超过N个item这种；但这些操作放在了最后一层，会造成召回和排序的空间浪费，也比较难嵌入到召回和排序中；而且参数是需要调优的，系统长时间处在非最优状态；
1. 注释：在系统设计出发点处，再次强调了rule-based的系统仅在考虑去重，没有将质量分考虑在内，但实际上submodular和MMR方法都是有考虑的；

## Approach
1. 形式化的定义问题：01向量y表示用户是否"喜欢"推荐结果，如果要把y\[i\]调整到y\[j\]的位置，那么希望G=sum(y\[i\]/j)能最大化，即尽量把好结果往前排；
1. 形式化的定义问题：定义两个item i和j是相似的，表示为P(y\[i\]==1 and y\[j\]==1) < P(y\[i\]==1) \* P(y\[j\]==1)，即他们如果同时出现，不大可能独立的成为一个好结果；
1. 用到的输入包括：a) 黑盒化的pointwise的质量分q\[i\]；b) 黑盒化的pair-wise的距离衡量D\[i\]\[j\]，这个距离不需要是一个严格的概率，可以是Jaccard距离等；
1. 

## Experiments

## References

