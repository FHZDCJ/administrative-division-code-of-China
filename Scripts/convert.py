import json

def trim_tree(node, target_level, field_filter):
    current_level = node.get("level")

    # 超过目标层级：直接丢弃
    if current_level > target_level:
        return None

    # 构建节点
    new_node = {}

    if field_filter["code"]:
        new_node["code"] = node.get("code")
    if field_filter["name"]:
        new_node["name"] = node.get("name")
    if field_filter["level"]:
        new_node["level"] = node.get("level")
    if field_filter["type"]:
        new_node["type"] = node.get("type")

    # 如果刚好是目标层级 → 不要 children
    if current_level == target_level:
        return new_node

    # 递归子节点
    children = node.get("children", [])
    new_children = []

    for child in children:
        trimmed = trim_tree(child, target_level, field_filter)
        if trimmed:
            new_children.append(trimmed)

    # 不允许空 children
    if new_children:
        new_node["children"] = new_children

    return new_node


def generate_linked_json(
    data,
    target_level,
    include_code=True,
    include_name=True,
    include_level=False,
    include_type=False
):
    if not (include_code or include_name):
        raise ValueError("code 和 name 至少需要输出一个")

    if target_level not in [1, 2, 3, 4]:
        raise ValueError("target_level 只能是 1~4")

    field_filter = {
        "code": include_code,
        "name": include_name,
        "level": include_level,
        "type": include_type
    }

    if isinstance(data, list):
        result = []
        for node in data:
            trimmed = trim_tree(node, target_level, field_filter)
            if trimmed:
                result.append(trimmed)
        return result
    else:
        return trim_tree(data, target_level, field_filter)

# =========================
# 写文件
# =========================
def save_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            separators=(",", ":")
        )


# =========================
# 批量导出配置
# =========================
EXPORT_CONFIGS = [
    # 2级
    {"level": 2, "name": "pc",   "code": False},
    {"level": 2, "name": "pc-code", "code": True},

    # 3级
    {"level": 3, "name": "pca",  "code": False},
    {"level": 3, "name": "pca-code", "code": True},

    # 4级
    {"level": 4, "name": "pcas", "code": False},
    {"level": 4, "name": "pcas-code", "code": True},
]


# =========================
# 主入口
# =========================
if __name__ == "__main__":
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for cfg in EXPORT_CONFIGS:
        result = generate_linked_json(
            data,
            target_level=cfg["level"],
            include_code=cfg["code"],
            include_name=True
        )

        filename = f"{cfg['name']}.json"
        save_json(result, filename)

        print(f"已生成：{filename}")

    print("全部导出完成")