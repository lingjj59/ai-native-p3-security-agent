# 第一次任务提交包 / 开题 v0.1

日期：2026-10-13。提交口径：仓库课程摘要第一章第 10 节 A/B 必做及 C 选做，同时提供 P3 开题；不是第二章 PaperManagement-Lab 的替代作业。课程平台、截止日期及成员信息待教师/用户补充。

## 交付索引

| 项目 | 本次材料 | 状态 |
| --- | --- | --- |
| 学期开题 | [一页 Brief](../brief.md)、[Intent](../problem-frame.md)、[分工/八任务](../plan.md)、[未决与授权](../open-questions.md) | 草案就绪；教师批准、姓名与结对待确认 |
| A 必做 | 根目录 [AGENTS.md](../../AGENTS.md)：定位、地图、三条约定、构建/测试 | 已提供 |
| A 阅读测试说明 | 见下方，100 字以内 | 导航自检；陌生 AI 独立阅读待复核 |
| B 必做 | [真实功能 GWT 与四项自检](../specification.md) | 已提供 8 条，含正向/负向/对抗 |
| C 选做 | [源码](../../src/p3_agent/runner.py)、[测试](../../eval/test_baseline.py)、本页 Trace 与反思 | 可执行模拟基线；实际运行记录见证据索引 |
| Harness | [仓库地图](../repository-map.md)、[命令与权限](../harness-manifest.md)、[恢复](../../release/README.md) | 已提供 |
| 可追溯性 | [验收矩阵](../acceptance-matrix.md)、[ADR](../adr/001-simulator-first.md)、[AI 披露](../ai-disclosure.md)、[证据说明](../../evidence/README.md) | 阶段状态与证据来源明确 |

## A：AI 阅读测试说明（100 字以内）

给陌生 AI 仅看 AGENTS.md，问“超时判定、授权门和测试在哪？”预期定位 reporting.py、controller.py、eval。当前只完成导航自检，独立阅读结果待复核。

复核时另开无历史上下文的 AI 会话，仅提供 AGENTS.md，保留提问、原回答和是否找到三个路径的结果；不把本次已读过全仓库的 AI 当作陌生读者。本次未伪造该独立运行。

## C：执行 Trace 摘要

开发顺序：读取仓库课题与贡献约定 → 固定本次提交边界 → 写 Spec/实现模拟切片 → 执行自动验证与三场景 → 检查 diff → Git 分支/提交/PR。没有调用目标网络或外部模型来运行产品。

产品运行：固定计划，Good/Bad 预期各 6 次检查、6 轮决策；Timeout 预期 1 次检查、2 轮决策（第二轮被预算门拒绝）。实际数字与源码 commit 以 `evidence/manifest.json` 和原始运行包为准。产品模型调用/Token/费用均为 0；开发 AI 会话工具调用总数、Token、轮次、费用为 unavailable，不能拿产品 0 冒充开发 0。

自动验证命令：`python -m unittest discover -s eval -v`、`python -m compileall -q src scripts eval`、`python scripts/check_docs.py`。正式输出保存在 `evidence/validation/`，本页不代替日志。三场景使用 `python scripts/run_demo.py --scenario <good|known-bad|timeout>`。

## C：反思（约 200 字）

这次先把授权门、证据和停止条件写成可观察的规格，再完成模拟闭环。正常、越权和超时都留下原始响应，使报告能区分确认问题与证据不足。没有把模拟结果写成真实服务验收，也没有把 AI 生成当作两名成员的独立贡献。当前仍缺模型调度、评价器和运行中撤权；这些属于后续里程碑，不用占位代码宣称完成。遇到真实目标、预算或课程批准未知时，应停在已有模拟范围，登记负责人和确认节点。下一步由组员独立重跑、解释关键路径，并请教师确认题目与授权，再扩展本地服务。

## 提交与人工核对

GitHub 是本次实际提交渠道；未向任何教师、邮件或课程平台发送。两名组员姓名/学号、结对组、教师审批、具体截止日期和人工签署待补；这些缺口不会被代码测试通过自动消除。后续使用[未决项](../open-questions.md)逐项关闭。
