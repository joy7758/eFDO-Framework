import hashlib
import json
import time

class EFDO_Generator:
    """
    eFDO (Evolutionary FAIR Digital Object) Sovereign ID Generator
    eFDO 主权标识符生成器
    
    Principles Implemented / 实现的原则:
    1. Evolutionary Reference (进化参照): Metadata is treated as DNA.
    2. Controlled Co-Prosperity (受控共荣): Hard-coded safety checks.
    """

    def __init__(self, owner_email):
        self.owner = owner_email
        self.standard_version = "eFDO-v1.0"

    def generate_pid(self, initial_data):
        """
        Generate an immutable Sovereign PID based on metadata content.
        基于元数据内容生成不可篡改的主权 PID。
        """
        # 1. DNA Construction (构建数字基因)
        # We combine user data with the 3 Core Principles to form the unique identity
        dna_structure = {
            "content": initial_data,
            "owner": self.owner,
            "principles": {
                "p1": "evolutionary_reference",
                "p2": "controlled_co_prosperity",
                "p3": "unknown_exploration"
            },
            "timestamp": time.time()
        }
        
        # Serialize to a standard string format (JSON)
        # 序列化为标准字符串
        dna_string = json.dumps(dna_structure, sort_keys=True)
        
        # 2. Hashing (哈希计算) - The "Digital Fingerprint"
        # Using SHA-256 to lock the identity
        # 使用 SHA-256 锁定身份
        pid_hash = hashlib.sha256(dna_string.encode('utf-8')).hexdigest()
        
        # Return the Sovereign ID (first 16 chars)
        return f"efdo:{pid_hash[:16]}"

# --- Quick Test / 快速测试 ---
if __name__ == "__main__":
    # Simulate creating an eFDO
    # 模拟创建一个 eFDO 对象
    my_generator = EFDO_Generator("joy7759@gmail.com")
    
    # Define some initial data (e.g., a research dataset)
    data_payload = {
        "project": "Carbon-Silicon-Bridge",
        "description": "Initial mutation test"
    }
    
    # Generate ID
    new_pid = my_generator.generate_pid(data_payload)
    
    print("-" * 30)
    print("eFDO Created Successfully! / eFDO 创建成功！")
    print(f"Owner (所有者): {my_generator.owner}")
    print(f"Sovereign PID (主权标识): {new_pid}")
    print("-" * 30)
