import numpy as np
import matplotlib.pyplot as plt


def montecarlo(times = 1000000, seed = 42):
    # 创建随机数发生器
    rng = np.random.default_rng(seed)

    # 定义p和theta
    p = rng.random(times)
    theta = rng.uniform(0, np.pi/2, times)

    # 计算两个式子的差分，得到对应的大小关系
    diff = np.cos(p * theta) - np.cos(theta)**p

    # 计算大于0的式子的个数，并将其与总体数相除得到总体的比率
    result = np.mean(diff >= 0)

    print(f"结果: {result * 100:.6f}%")

    # 此处仅取部分的点进行可视化，当点数到达100万的时候可视化出来的图像非常容易卡顿
    ax = plt.figure(figsize=(10, 7)).add_subplot(111, projection='3d')
    s = ax.scatter(p[::500], theta[::500], diff[::500], c=diff[::500], cmap='viridis', s=2)
    ax.set_xlabel('p')
    ax.set_ylabel('theta')
    ax.set_zlabel('diff')
    plt.colorbar(s)
    plt.show()





montecarlo()

