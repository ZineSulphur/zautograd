# zautograd

A mini project for auto grad learning
学习自动微分的一个小项目

## 项目内容

### 自动微分方式

#### 前向传播

前向模式（Forward Automatic Differentiation，也叫做 tangent mode AD）或者前向累积梯度（前向模式）。

前向模式从计算图的起点开始，沿着计算图边的方向依次向前计算，最终到达计算图的终点。它根据自变量的值计算出计算图中每个节点的值 以及其导数值，并保留中间结果。一直得到整个函数的值和其导数值。整个过程对应于一元复合函数求导时从最内层逐步向外层求导。

以 z = lnx + xy - siny 的 dz/dx 为例:
|Forward Primal Trace|Forward Tangent Trace|
|---|---|
|x = 2|dx = 1|
|y = 5|dy = 0|
|t1 = lnx = ln2|dt1 = dx/x = 1/2|
|t2 = xy = 2x5|dt2 = ydx + xdy = 1x5+5x0|
|t3 = siny = sin5|dt3 = cosydy = cos5 x 0|
|t4 = t1 + t2 = 0.693+10|dt4 = dt1 + dt2 = 0.5+5|
|t5 = t4 - t3 = 10.693+0.959|dt5 = dt4 - dt3 = 5.5 -0|
|y = t5 = 11.652|dy/dx = dt5/dx = 5.5|

可见前向传播是在进行相应计算的同时计算此时的中间变量的微分。最后根据链式法则求最终值

同时我们可以注意到，当我们求dz/dx时，dx的初始值为1，dy为0。若初始值为dx=0，dy=1时，我们就可以求dz/dy即z对y的梯度。

#### 反向传播

以 z = lnx + xy - siny 的 dz/dx 为例, vi = dz/dti，微分阶段从下往上计算:
|Forward Primal Trace|Reverse Adjoint Trace|
|---|---|
|x = 2|dx = 5.5|
|y = 5|dy = 1.762|
|t1 = lnx = ln2|dx = dx + v1/x = 5.5|
|t2 = xy = 2x5|dy = dy + v2 * dt2/dy = dy + v2 * x = 1.716|
||dx = v2 * dt2/dx = v2 * y = 5|
|t3 = siny = sin5|dy = v3 * dt3/dy = v3 * cosy = -0.284|
|t4 = t1 + t2 = 0.693+10|v1 = v4 * dt4/dt1 = v4 * 1 = 1|
||v2 = v4 * dt4/dt2 = v4 * 1 = 1|
|t5 = t4 - t3 = 10.693+0.959|v3 = v5 * dt5/dt3 = v5 * -1 = -1|
||v4 = v5 * dt5/dt4 = v5 * 1 = 1|
|y = t5 = 11.652|v5 = dy = 1|

可以看见反向传播是以链式法则为基础，从结果反向推导至需要的变量，最后求出其梯度。

如果不同的式子中都有同个变量，则将不同式子的梯度值加起来。

因此在开始计算前需要将因变量的梯度设为1，其它梯度都设为0。

### 自动微分方法

自动微分方法，主要分为基本表达式法，操作符重载法，源码转换法三种

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

#### demo.ipynb

以上实现方法的demo，包含一个简单的函数的求梯度例子和运行结果。

### 简易神经网络

#### ad.nn

1. **Module**

神经网络模块基类。

- zero_grad(self): 这个方法用于将模块中所有参数的梯度重置为0。这通常在每次反向传播之前调用，以清除上一次迭代的梯度。
- parameters(self): 这个方法返回一个包含模块所有参数的列表。在基类中,它返回一个空列表，因为基础的 Module 类并没有任何参数。但在子类中，我们会重写这个方法，返回子类特有的参数列表。

2. **Neuron**

神经网络神经元。

- __init__(self, nin, nonlin=True): 神经元构造函数，nin为输入数量，nonlin表示该神经元是否为线性函数神经元。同时初始化权重值self.w和偏置self.b。
- __call__(self, x): 定义神经元前向传播逻辑，即激活值act为输入x和权重self.w的点积，加上偏置self.b。若nonlin=True则加上ReLU函数进行激活。
- paramerters(self): 返回神经元所有参数。
- __repr__(self): 返回字符串用于表示神经元。

3. **Layer**

神经网络层，由多个神经元组成。

- __init__(self, nin, nout, \*\*kwargs): 层构造函数，nin为输入数量，nout为输出数量，\*\*kwargs用于接受其它参数，如给神经元的nonlin。同时构建该层的神经元列表self.neurons。
- __call__(self, x): 定义层前向传播逻辑，给定输入x给层中所有神经元，返回一个神经元的输出或者多个神经元的输出列表。
- paramerters(self): 返回层所有参数。
- __repr__(self): 返回字符串用于表示层。

4. **MLP**

神经网络，由多层组成。

- __init__(self, nin, nouts): 层构造函数，nin为输入数量，nouts为每层输出数量。nin添加到nouts为sz表示层大小，self.layers根据sz[i]和sz[i+1]相邻两层大小构建layer对象列表。
- __call__(self, x): 定义MLP前向传播逻辑，给定输入x给层中所有层，将每层输出作为下一层输入，最后返回最后一层输出。
- paramerters(self): 返回MLP所有参数。
- __repr__(self): 返回字符串用于表示MLP。

#### 简易训练步骤

1. 创建训练循环
2. 构建模型MLP
3. 构建损失函数loss
4. 正向计算
5. 梯度清零和反向传播
6. 更新相关参数
7. 下个循环

## 参考资料

[从零实现自动微分框架](https://garden.maxieewong.com/000.wiki/%E4%BB%8E%E9%9B%B6%E5%AE%9E%E7%8E%B0%E8%87%AA%E5%8A%A8%E5%BE%AE%E5%88%86%E6%A1%86%E6%9E%B6/)

[micrograd](https://github.com/karpathy/micrograd/tree/master)

[AISystem](https://github.com/chenzomi12/AISystem/tree/main/05Framework/02AutoDiff)
