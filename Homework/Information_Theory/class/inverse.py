def find_inverse_elements(p):
    # 初始化存储逆元的列表
    additive_inverse = [0] * p
    multiplicative_inverse = [0] * p

    # 计算加法逆元
    for i in range(p):
        additive_inverse[i] = (-i) % p

    # 计算乘法逆元
    for i in range(1, p):
        for j in range(1, p):
            if (i * j) % p == 1:
                multiplicative_inverse[i] = j
                break

    # 返回逆元
    return additive_inverse, multiplicative_inverse


if __name__ == "__main__":
    # 设置素数
    p = 7

    # 求解逆元
    additive_inverse, multiplicative_inverse = find_inverse_elements(p)

    # 打印结果
    print(f"模 {p} 的有限域上的全部非零元素的加法逆元是: {additive_inverse[1:]}")
    print(f"模 {p} 的有限域上的全部非零元素的乘法逆元是: {multiplicative_inverse[1:]}")
