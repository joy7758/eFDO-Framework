# eFDO Sovereign DID Generator v1.0
# Standard: W3C Decentralized Identifiers (DIDs) v1.0
# Copyright (c) 2026 Zhang Bin (joy7759@gmail.com)

import hashlib
import json
import base64
from datetime import datetime

def generate_efdo_did(specimen_path):
    with open(specimen_path, 'r') as f:
        data = json.load(f)

    # 1. 提取核心性状作为身份指纹
    trait_str = json.dumps(data['traits'], sort_keys=True)
    
    # 2. 生成基于内容的哈希 (Content-Addressable)
    # 这确保了如果有人改了数据，DID 就会失效
    content_hash = hashlib.sha256(trait_str.encode()).hexdigest()
    
    # 3. 构造 eFDO 专属 DID 方法: did:efdo:<hash>
    did_id = f"did:efdo:{content_hash[:32]}"
    
    # 4. 构造符合 W3C 标准的 DID Document (简版)
    did_document = {
        "@context": "https://www.w3.org/ns/did/v1",
        "id": did_id,
        "controller": "did:efdo:admin:zhangbin",
        "created": datetime.now().isoformat(),
        "verificationMethod": [{
            "id": f"{did_id}#key-1",
            "type": "Ed25519VerificationKey2020",
            "controller": did_id,
            "publicKeyMultibase": "z6MkpTHR8VNsLj7o8aR" # 示意公钥
        }]
    }
    
    # 5. 更新标本数据
    data['did'] = did_id
    data['did_document'] = did_document
    
    with open(specimen_path, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"✅ 身份确权成功！")
    print(f"🏷️ 标本 DID: {did_id}")
    print(f"📜 DID Document 已注入 specimen.json")

if __name__ == "__main__":
    generate_efdo_did('specimen.json')
