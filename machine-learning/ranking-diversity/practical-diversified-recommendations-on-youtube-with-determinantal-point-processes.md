# practical diversified recommendations on youtube with determinantal point processes
[pdf](https://jgillenw.com/cikm2018.pdf)

## logs
* [ 2019-12-10 14:57:32 ] finish
* [ 2019-12-10 14:18:14 ] begin
* [ 2019-12-10 13:28:02 ] hold
* [ 2019-12-10 13:00:41 ] begin
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
### 形式化的定义问题
1. 01向量y表示用户是否"喜欢"推荐结果，如果要把y\[i\]调整到y\[j\]的位置，那么希望G=sum(y\[i\]/j)能最大化，即尽量把好结果往前排；
1. 定义两个item i和j是相似的，表示为P(y\[i\]==1 and y\[j\]==1) < P(y\[i\]==1) \* P(y\[j\]==1)，即他们如果同时出现，不大可能独立的成为一个好结果；
1. 用到的输入包括：a) 黑盒化的pointwise的质量分q\[i\]；b) 黑盒化的pair-wise的距离衡量D\[i, j\]，这个距离不需要是一个严格的概率，可以是Jaccard距离等；
### DPP方法
1. DPP是一种子集概率函数，对于给定集合的每个子集，会给出一个非零估值，并且这些估值的和为1； 
1. 如果定义正样本集的下标集为Y，则dpp的一种定义为 score(Y) = det(L[Y])，dpp(Y) = score(Y) / sum(score(all Y))，det是行列式，Y是一个矩阵，L[i,i] = q[i]\*q[i]，L[i,j (i!=j)] = dis\[i, j\]；
1. 这里出现了一个很漂亮的性质：sum(det(all Y)) = det(L + I)，即分母项可以快速求得，不用算排列组合的复杂度，前提是L是PSD的；
1. 在|Y|==2的情况下，L的行列式实际上是q1\*q2 - dis[1,2]*dis[2,1]，即质量的乘积减去距离的乘积；高维的情况会更复杂一些，但实际上会类似；
1. 进一步的，定义dis\[i,j\] = alpha \* q\[i\] \* q\[j\] \* exp(-D\[i,j\]/(2\*sigma\*sigma))；alpha=1等价于RBF；0<alpha<1时；注意按照DPP的定义，要求L是一个半正定矩阵，alpha不能太大，所以需要一些trick来保证；
1. 注意论文4.2节中一个用词晦涩导致难以理解的坑：`"consider" all items to be more diverse`，这里的consider不是“导致”，而是“当认为”的意思；即当我们认为候选集比较多样的时候，可以设置alpha比较小；反之当我们认为候选集多样性不足的时候，应该把alpha设大，来增加多样性的贡献；
### 训练方法及推广
1. 这个模型只有alpha sigma两个参数，所以训练模型只需要grid search即可；训练数据用一天的youtube mobile日志，大约40k；
1. 因为给出了概率预估，所以可以用loglikelyhood训练，使得每次推荐的set的点击集合Y的概率dpp(Y)能最大化，而根据公式，dpp(Y) = det(L[Y])/det(L+I)是可以在不求出全部排列组合的情况下单点求得的；
1. 除了仅包括alpha和sigma的版本之外，可以进一步将参数复杂化，质量分可以是一个向量，表示多个不同角度的质量考量，L\[i,j\] = f(q[i]) * g(emb[i])<sub>T</sub> * g(emb[j]) * f(q[j]) + beta*I(i==j)；这里f是一个把向量变成标量的函数，一般是一个浅层NN，g是一个向量到向量的函数，一般是一个比较深的NN；和之前的alpha sigma参数不同，这个公式构造出来的L矩阵一定是PSD的。
### 线上应用策略
1. 给定N(~几百)个候选item，以及他们的质量分q和向量emb；
1. 每次取参数k(~10)，从剩下的候选集里面取出k个组成一个集合，使得其dpp概率最大；
1. 求得大小为k的最优子集是NP-HARD的，所以只能submodular的做，每次贪心的取一个加进去之后最优的item；

## Experiments
### 实验设置
1. Fuzzy dedup：不允许新增的item_j和集合内已有的任何一个item_i的距离D\[i,j\]<thr；
1. Sliding window：m个item的窗口里面只允许有n个的距离小于thr；
1. Smooth score penalty：每个item都要和前序item的加权向量和算一个相似度作为惩罚项；
1. DPP：只包含alpha和sigma的简单DPP方法；
1. Deep DPP：变形后带神经网络的DPP方法；
### 实验结果

|Strategy|Satisfied homepage wachers|
|--------|--------------------------|
|Fuzzy dedup| -0.05% |
|Sliding window| -0.26% |
|Smooth score penalty| -0.41% |
|DPP| +0.63% |
|Deep DPP| +1.72% |

1. DPP系列方法都是正向收益的，而且除了用户级别的满意比例，在时长上也有收益；
1. DPP方法已经从mobile推广到youtube的所有场景；
1. Deep DPP虽然效果更好，但对于排序结果分布的改变太大，导致下游的业务逻辑需要大改，因此没有推广，还在继续调参优化中；
1. 随着实验周期的变长，DPP还进一步带来了用户活跃度和渗透率的提升；


## References

