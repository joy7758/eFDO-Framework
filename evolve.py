import json
import random
import hashlib
import time

def generate_efdo_hash(data):
    # 实现你的 HDF5 哈希逻辑简化版
    content = json.dumps(data, sort_keys=True)
    return "efdo:" + hashlib.sha256(content.encode()).hexdigest()[:16]

def mutate():
    # 1. 加载当前的数字标本
    with open('specimen.json', 'r') as f:
        specimen = json.load(f)

    print(f"--- 进化前 (第 {specimen['generation']} 代) ---")
    print(f"当前 PID: {specimen['pid']}")

    # 2. 模拟突变 (进化参照论：属性随机波动)
    mutation_rate = 0.1
    trait_to_mutate = random.choice(['accuracy', 'speed', 'robustness'])
    change = random.uniform(-mutation_rate, mutation_rate)
    
    specimen['traits'][trait_to_mutate] = round(specimen['traits'][trait_to_mutate] + change, 2)
    specimen['generation'] += 1
    
    # 3. 记录进化历史
    log_entry = f"Gen {specimen['generation']}: {trait_to_mutate} changed by {change:.2f}"
    specimen['evolution_history'].append(log_entry)

    # 4. 生成新的主权 PID (每个版本都是唯一的)
    specimen['pid'] = generate_efdo_hash(specimen['traits'])

    # 5. 保存进化后的状态
    with open('specimen.json', 'w') as f:
        json.dump(specimen, f, indent=2)

    print(f"\n>>> 进化完成！")
    print(f"突变属性: {trait_to_mutate}")
    print(f"新代数: {specimen['generation']}")
    print(f"新 PID: {specimen['pid']}")
    print("------------------------------")

if __name__ == "__main__":
    mutate()
