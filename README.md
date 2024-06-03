# zautograd

A mini project for auto grad learning
学习自动微分的一个小项目

## 项目内容

### ad

自动微分方法

#### ad.adlib

基本表达式法也叫做元素库（Elemental Libraries），程序中实现构成自动微分中计算的最基本的类别或者表达式，并通过调用自动微分中的库，来代替数学逻辑运算来工作。然后在函数定义中使用库公开的方法，这意味着在编写代码时，手动将任何函数分解为基本操作。

基本表达式法的优点：

- 实现简单，基本可在任意语言中快速地实现为库

基本表达式法的缺点：

- 用户必须使用库函数进行编程，而无法使用语言原生的运算表达式
- 另外实现逻辑和代码也会冗余较长，依赖于开发人员较强的数学背景

#### ad.adoo

操作符重载法通过重载编程语言操作符来实现计算和自动微分。

在具有多态特性的现代编程语言中，运算符重载提供了实现自动微分的最直接方式，利用了编程语言的第一特性（first class feature），重新定义了微分基本操作语义的能力。

操作符重载法的优点：

- 实现简单，只要求语言提供多态的特性能力
- 易用性高，重载操作符后跟使用原生语言的编程方式类似

操作符重载法的缺点:

- 需要显式的构造特殊数据结构和对特殊数据结构进行大量读写、遍历操作，这些额外数据结构和操作的引入不利于高阶微分的实现
- 对于一些类似 if，while 等控制流表达式，难以通过操作符重载进行微分规则定义。对于这些操作的处理会退化成基本表达式方法中特定函数封装的方式，难以使用语言原生的控制流表达式

#### ad.adsct

源码转换（Source Code Transformation，SCT）是最复杂的，实现起来也是非常具有挑战性。

源码转换的实现提供了对编程语言的扩展，可自动将算法分解为支持自动微分的基本操作。通常作为预处理器执行，以将扩展语言的输入转换为原始语言。简单来说就是利用源语言来实现领域扩展语言 DSL 的操作方式。

## 参考资料

[从零实现自动微分框架](https://garden.maxieewong.com/000.wiki/%E4%BB%8E%E9%9B%B6%E5%AE%9E%E7%8E%B0%E8%87%AA%E5%8A%A8%E5%BE%AE%E5%88%86%E6%A1%86%E6%9E%B6/)

[micrograd](https://github.com/karpathy/micrograd/tree/master)

[AISystem](https://github.com/chenzomi12/AISystem/tree/main/05Framework/02AutoDiff)
