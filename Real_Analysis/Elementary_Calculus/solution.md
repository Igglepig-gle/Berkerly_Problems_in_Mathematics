# 1.1 Elementary Calculus

## Problem 1.1.1



### 前置知识：



#### Jessen不等式



若 $f$ 是定义在区间 $I$ 上的凸函数，则对于任何 $x_1, x_2, \dots, x_n \in I$ 以及满足 $\sum_{i=1}^n \lambda_i = 1$ 的非负权重 $\lambda_i \ge 0$，下式成立：
$$
f\left(\sum_{i=1}^n \lambda_i x_i\right) \le \sum_{i=1}^n \lambda_i f(x_i)
$$
**数学归纳法**：



当n = 2时，根据凸函数的定义，对于 $\lambda_1, \lambda_2 \ge 0$ 且 $\lambda_1 + \lambda_2 = 1$：
$$
f(\lambda_1 x_1 + \lambda_2 x_2) \le \lambda_1 f(x_1) + \lambda_2 f(x_2)
$$
此步由凸函数的定义直接得出，命题成立。



假设当 $n = k$ 时命题成立，即：
$$
f\left(\sum_{i=1}^k \lambda_i x_i\right) \le \sum_{i=1}^k \lambda_i f(x_i)
$$
当$n = k + 1$时，为了利用归纳假设，我们提取出最后一项：
$$
\sum_{i=1}^{k+1} \lambda_i x_i = (1-\lambda_{k+1}) \left( \sum_{i=1}^k \frac{\lambda_i}{1-\lambda_{k+1}} x_i \right) + \lambda_{k+1} x_{k+1}
$$
令 $x' = \sum_{i=1}^k \frac{\lambda_i}{1-\lambda_{k+1}} x_i$。因为 $\sum_{i=1}^k \frac{\lambda_i}{1 - \lambda_{k+1}} = 1$，因此 $x'$ 是前 $k$ 个点的凸组合。

利用 $n=2$ 的情况：
$$
f\left((1-\lambda_{k+1})x' + \lambda_{k+1}x_{k+1}\right) \le (1-\lambda_{k+1})f(x') + \lambda_{k+1}f(x_{k+1})
$$
再对 $f(x')$ 利用 $n=k$ 的归纳假设：
$$
f(x') = f\left(\sum_{i=1}^k \frac{\lambda_i}{1 - \lambda_{k+1}} x_i\right) \le \sum_{i=1}^k \frac{\lambda_i}{1 - \lambda_{k+1}} f(x_i)
$$
代回上式：
$$
f\left(\sum_{i=1}^{k+1} \lambda_i x_i\right) \le (1 - \lambda_{k+1}) \left[ \sum_{i=1}^k \frac{\lambda_i}{1 - \lambda_{k+1}} f(x_i) \right] + \lambda_{k+1} f(x_{k+1})
$$

$$
f\left(\sum_{i=1}^{k+1} \lambda_i x_i\right) \le \sum_{i=1}^{k+1} \lambda_i f(x_i)
$$

**证毕。**



假如函数为凹函数那么不等式的方向相反



### 题解



由于在给定区间内，$\cos(\theta)$ 和 $\cos(p\theta)$ 均大于等于 0，我们可以对等式两边取对数。如果对数形式的不等式成立，则原不等式成立：
$$
\ln(\cos(p\theta)) \ge p \ln(\cos(\theta))
$$
构造函数：$f(x) = \ln(\cos(x))$，其中 $x \in [0, \pi/2]$。

上述不等式可以写为：
$$
f(px) \ge p f(x)
$$
计算得到$f''(x) = -\sec^2(x)$, 由于 $\sec^2(x) > 0$，所以 $f''(x) < 0$, 则 $f(x) = \ln(\cos(x))$ 在 $[0, \pi/2]$ 上是一个严格凹函数



于是利用Jessen不等式得到
$$
f(px) = f(p \cdot x + (1-p) \cdot 0) \ge p f(x) + (1-p) f(0)
$$
由于$f(0) = \ln(\cos(0)) = 0$
$$
f(px) \ge p f(x)
$$


