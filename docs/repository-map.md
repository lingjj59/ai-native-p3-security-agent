# 仓库地图

| 路径 | 内容 / 状态 |
| --- | --- |
| 根目录两份课程文档 | 课程要求与长版方案，保留来源和待确认说明 |
| AGENTS.md | AI 导航、三条约定、实际命令和停止规则 |
| docs/ | 开题 Brief、Intent、Spec/GWT、矩阵、状态、计划、ADR、未决项、首次提交 |
| src/p3_agent/ | registry、controller、executor、reporting、runner，已实现模拟固定基线 |
| lab/public-fixtures/ | Good、Known Bad、Timeout 的公开虚构数据 |
| eval/ | 产品行为与边界的 unittest |
| evaluator/ | 只读评价器设计入口，尚无可执行评价器 |
| evidence/ | 提交证据索引；runs 下原始运行、版本、报告和哈希 |
| review/ | 实验、Change、Finding、结对和签署的后续流程 |
| release/ | 启动、停止、重置、恢复、限制 |
| scripts/ | 场景 CLI 和文档完整性检查 |
| .github/workflows/ | 自动测试、编译、文档检查和 Good 烟雾运行 |

关键路径：`scripts/run_demo.py` → `runner.run` 固定 ORDER → `Controller.admit` → `Simulator.execute` → `classify` → 原始 events 与 report。更改超时解释先读 reporting；更改权限先读 registry/controller；新场景放 lab，不能让报告层伪造 executor 事件。
