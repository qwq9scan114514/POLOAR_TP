import math

H_PLANCK = 6.62607015e-34    # 普朗克常数 (J·s)
K_BOLTZMANN = 1.380649e-23   # 玻尔兹曼常数 (J/K)
C_SPEED = 299792458          # 光速 (m/s)
NA = 6.02214076e23           # 阿伏伽德罗常数 (mol^-1)
LN10 = math.log(10)          # 用于熵到 log10 复杂度的换算

def calculate_traversal_logic(name, mass_kg, entropy_total, rate_hz):
    """
    基于 R = (eta * E) / (h * Omega) 且 Phi = 1 的计算
    """
    # 能量 E = mc^2
    energy = mass_kg * (C_SPEED ** 2)
    
    # 资源预算 (Budget): log10(E / (h * R))
    # 代表系统在当前频率下，理论能支持的最大复杂度步数
    log10_budget = math.log10(energy / (H_PLANCK * rate_hz))
    
    # 地图大小 (Map/Complexity): log10(Omega) = S / (kb * ln10)
    # 代表系统真实的微观热力学状态空间
    if entropy_total == 0:
        log10_omega = 0.0
    else:
        log10_omega = entropy_total / (K_BOLTZMANN * LN10)
    
    # 杠杆率 (Leverage): log10(Omega) / log10(Budget)
    # 描述系统是对资源的“保守利用”还是“疯狂借贷”
    leverage = log10_omega / log10_budget if log10_budget != 0 else 0
    
    return {
        "name": name,
        "energy": energy,
        "log_budget": log10_budget,
        "log_omega": log10_omega,
        "leverage": leverage
    }

samples = [
    # 光子: 绝对原点 (1eV 能级)
    {
        "name": "光子 (1eV)",
        "mass": 1.6e-19 / (C_SPEED**2),
        "entropy": 0,
        "rate": 2.417e14  # E/h
    },
    # 铁原子: 无机死物 (1个原子)
    # 摩尔熵 27.3 J/mol·K -> 单个原子熵
    {
        "name": "单质铁 (Fe)",
        "mass": (55.845 / 1000) / NA,
        "entropy": 27.3 / NA,
        "rate": 9.79e12   # 德拜频率
    },
    # 金刚石: 无机死物 (1个原子)
    # 摩尔熵 2.38 J/mol·K -> 单个原子熵
    {
        "name": "金刚石 (C)",
        "mass": (12.01 / 1000) / NA,
        "entropy": 2.38 / NA,
        "rate": 4.65e13   # 德拜频率
    },
    # 中子星单元: 量子极限
    # 中子质量，极低熵，核力频率
    {
        "name": "中子星单元",
        "mass": 1.67e-27,
        "entropy": 0.01 * K_BOLTZMANN * LN10,  # 极低熵
        "rate": 1e22      # 核力频率
    },
    # 原始 RNA: 生命逻辑起点 (100个核苷酸)
    # 100nt, 摩尔熵估算 8000 J/mol·K
    {
        "name": "自复制 RNA",
        "mass": 5.48e-23,
        "entropy": 8000 / NA,
        "rate": 1e8       # 构象翻转频率
    },
    # 小鼠 N80: 意识层级 (0.8微克脑组织)
    # 质量 8e-10kg, 比熵 3.5 J/g/K -> 2.8e-3 J/K
    {
        "name": "小鼠 N80",
        "mass": 8e-10,
        "entropy": 2.8e-3,
        "rate": 12.72     # 脑电特征频率
    },
    # 普朗克黑洞: 微观奇点极限
    # 最小黑洞，普朗克质量量级
    {
        "name": "普朗克黑洞",
        "mass": 1.95e9 / (C_SPEED**2),  # E=1.95e9 J
        "entropy": 2.73 * K_BOLTZMANN * LN10,  # log10(Omega)=2.73
        "rate": 1.85e43   # 普朗克频率
    },
    # 太阳质量黑洞: 宏观奇点
    # 贝肯斯坦-霍金熵
    {
        "name": "太阳质量黑洞",
        "mass": 1.989e30,  # 太阳质量
        "entropy": 10**77.3 * K_BOLTZMANN * LN10,  # 巨大熵
        "rate": 1e4       # 霍金辐射频率
    }
]

# 输出原始数据表格
print("\n")
print("原始数据表格")
print(f"{'系统':<15} | {'质量 (kg)':<15} | {'熵 (J/K)':<15} | {'反应率 (Hz)':<15}")

for s in samples:
    mass_str = f"{s['mass']:.2e}"
    entropy_str = f"{s['entropy']:.2e}"
    rate_str = f"{s['rate']:.2e}"
    print(f"{s['name']:<15} | {mass_str:<15} | {entropy_str:<15} | {rate_str:<15}")

# 输出计算结果表格
print("\n")
print("计算结果")
print(f"{'系统':<15} | {'能效预算(logB)':<18} | {'地图复杂度(logΩ)':<20} | {'杠杆率(Ω/B)'}")


for s in samples:
    res = calculate_traversal_logic(s['name'], s['mass'], s['entropy'], s['rate'])
    
    # 针对小鼠这种爆炸数据进行科学计数展示
    if res['log_omega'] > 1e6:
        omega_str = f"{res['log_omega']:.2e}"
        leverage_str = f"{res['leverage']:.2e}"
    else:
        omega_str = f"{res['log_omega']:.2f}"
        leverage_str = f"{res['leverage']:.2f}"
        
    print(f"{res['name']:<15} | {res['log_budget']:<18.2f} | {omega_str:<20} | {leverage_str}")

