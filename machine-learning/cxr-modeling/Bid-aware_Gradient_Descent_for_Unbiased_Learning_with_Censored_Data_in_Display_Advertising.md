# Bid-aware Gradient Descent for Unbiased Learning with Censored Data in Display Advertising 
[pdf](https://www.kdd.org/kdd2016/papers/files/adp0028-zhangA.pdf)

## logs
* [ 2019-12-18 09:57:22 ] hold
* [ 2019-12-18 09:08:51 ] begin

## tags
* Yahoo
* unbiased learning
* cencored data
* RTB
* KDD 2016
* click through rate
* missing data

## Highlights
1. 通过把bidding信息引入到梯度中，来建模曝光数据收集有偏的问题，2015-09在雅虎上线后，AUC+2.97%，cpc-9.3%；

## Problem
1. 要求在整个流量空间上预估CTR和CVR，但只能收集到曝光后的数据，会存在样本分布有偏，价格高的样本因为胜出概率大，收集到的概率也大；
1. 传统的机器学习有应对missing data的方法，但是需要一个先验；折中的办法是做一些随机出价；
! [bias](bid-aware/figure1-biased.png)

## Related work
1. 用户反馈预估，也就是CTR/CVR预估；
1. RTB优化，一般来说二价拍卖最优策略是说真话，但加上容量和预算限制之后就不是了；在真实出价的基础上，会有一些不同的动态折价策略；
1. 有偏的离线评估，在线调优模型昂贵且危险，用历史数据来校正会便宜和安全一些；当数据采样模型已知且稳定，并且样本空间探索充分的情况下，可以用剔除采样的办法；也有人用强化学习；
1. miss-data学习，是推荐系统的经典问题，经常遇到只有隐式反馈的问题，一般通过各种负样本采样的办法解决；

## Approach

## Experiments

## References
* [知乎-三疯兰尼斯特-Aside: DSP的bidding算法](https://zhuanlan.zhihu.com/p/32664649)
* [知乎-三疯兰尼斯特-Algorithm-LR Bias和Q分布](https://zhuanlan.zhihu.com/p/31529643)
