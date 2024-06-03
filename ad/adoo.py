# the operateror overload method of autograd

class Value():
    def __init__(self, data, _children=(), _op=''):
        self.data = data  # 数据
        self.grad = 0      # 梯度
        # DAG图相关内容
        self._backward = lambda: None
        self._prev = set(_children)
        # 记录当前操作
        self._op = _op

    def backward(self):
        # 拓扑排序
        topo = []
        visited = set()
        # DFS
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        # 应用链式法则，反向传播求出梯度
        self.grad = 1
        for v in reversed(topo):
            v._backward()
            
    # 重载加法 self + other
    def __add__(self, other):
        # 判断other类型并转换成Value类型
        other = other if isinstance(other, Value) else Value(other)
        # 计算输出
        out = Value(self.data + other.data, (self, other), '+')

        # 反向传播计算梯度
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward

        return out
    
    
    # 重载乘法
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward

        return out
    
    # 重载乘方
    def __pow__(self, other):
        assert isinstance(other, (int, float)), "only supporting int/float"
        out = Value(self.data ** other, (self,), f'**{other}')

        def _backward():
            self.grad += (other * self.data**(other - 1)) * out.grad
        out._backward=_backward

        return out
    
    def __neg__(self): # -self
        return self * -1
    
    def __radd__(self, other): # other + self
        return self + other
    
    def __sub__(self, other): # self - other
        return self + (-other)
    
    def __rsub__(self, other): # other - self
        return other + (-self)
    
    def __rmul__(self, other): # other * self
        return self * other
    
    def __truediv__(self, other): # self / other
        return self * other ** -1
    
    def __rtruediv__(self, other): # other / self
        return other * self ** -1
    
    def __repr__(self) -> str:
        return f"Value(data={self.data}, grad={self.grad})"
