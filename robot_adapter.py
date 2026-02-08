import json, random
def run():
    path = 'specimen.json'
    try:
        with open(path, 'r') as f: data = json.load(f)
        t, temp = round(random.uniform(20,60), 2), round(random.uniform(30,90), 2)
        is_h = t > 55 or temp > 85
        data['industrial_metrics'] = {"joint_torque_nm": t, "motor_temp_c": temp}
        data['fatigue_index'] = 0.99 if is_h else round((t/100 + temp/200), 2)
        data['state'] = "CRITICAL_HALT" if is_h else "OPERATIONAL"
        with open(path, 'w') as f: json.dump(data, f, indent=2)
        print(f"✅ 工业数据注入：{t} Nm / {temp} °C")
    except: print("❌ 请先运行 python3 evolve.py")
if __name__ == "__main__": run()
