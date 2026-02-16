# Rule Builder

自用规则聚合脚本：拉取上游规则并生成 `Surge(.list)` 和 `Clash(.yaml)` 文件。

## Files

- `rule.py`: 主脚本
- `sources.yaml`: 规则配置
- `rule.list` / `rule.yaml` / `x.list` / `x.yaml`: 生成结果
- `manifest.json`: 抓取状态和输出统计

## Run

```bash
./venv/bin/python rule.py
```

## Config

编辑 `sources.yaml`：

- `names`: 上游规则名（自动拉取 Surge/Clash 对应规则）
- `suffix`: 追加 `DOMAIN-SUFFIX`
- `keyword`: 追加 `DOMAIN-KEYWORD`
