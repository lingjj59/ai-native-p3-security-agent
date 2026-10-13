# 证据规则

`manifest.json` 索引本次选定的真实**模拟器运行**，`validation/` 保存自动检查输出；`runs/<run_id>/` 保存原始观察、报告、Fixture 快照、版本和 SHA256。普通新运行默认被 Git 忽略，需先核查再显式 `git add -f` 提交要交付的 run。

每个运行包：metadata.json / fixture.json / events.jsonl / report.json / checksums.json。Evidence ID 为 `<run_id>:E序号`，报告引用本 run 的事件，不跨 run 拼接。来源 `fixture_demo`、强度 `OBSERVED`；没有独立执行者签署，不能写 `REPRODUCED`。

manifest 不是教师签署；哈希不是真实性证明。没有 report/checksums 的中断 run 必须保持“未完成”。测试日志与模拟报告分别保存，开发 AI 的工具调用或 Token 不混入产品成本。

首次冻结源码后，可在尚无 manifest 的干净 checkout 执行 `python scripts/collect_evidence.py`，自动检查并采集三场景。已有提交清单时脚本拒绝覆盖，日常复跑使用 run_demo。`.gitattributes` 固定证据原始字节，避免跨平台换行转换使哈希失效。
