import requests
import os

# 下载源规则
url = "https://raw.githubusercontent.com/Cats-Team/AdRules/main/mosdns_adrules.txt"
response = requests.get(url)
lines = response.text.splitlines()

# 创建 output 文件夹
os.makedirs("output", exist_ok=True)

# 转换规则为 hosts 格式
hosts_lines = []
for line in lines:
    line = line.strip()
    if line.startswith("domain:"):
        domain = line.replace("domain:", "").strip()
        hosts_lines.append(f"0.0.0.0 {domain}")

# 写入 hosts 文件
with open("output/hosts.txt", "w") as f:
    f.write("\n".join(hosts_lines))

print("✅ Hosts 文件已生成")
