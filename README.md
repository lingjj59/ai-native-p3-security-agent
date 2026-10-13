# AI 原生工程实践 · P3 授权边界测试 Agent

本仓库包含 P3 开题、第一章首次任务提交材料及可运行的离线模拟基线，作为后续实施、结对审查和验收的共同依据。

## 第一次提交入口

从 [第一次任务提交包](docs/submissions/first-submission.md) 开始：包括 [一页开题卡](docs/brief.md)、[AGENTS.md](AGENTS.md)、[GWT 与四项自检](docs/specification.md)、[验收矩阵](docs/acceptance-matrix.md)、AI 披露与 Trace 反思。组员姓名/学号、结对组和教师审批明确保留待确认。

## 快速运行

需要 Python 3.11+，在仓库根目录执行，无需安装依赖或模型密钥：

```text
python -m unittest discover -s eval -v
python scripts/check_docs.py
python scripts/run_demo.py --scenario good
python scripts/run_demo.py --scenario known-bad
python scripts/run_demo.py --scenario timeout
```

Good 完成六项；Known Bad 确认 T02 模拟越权；Timeout 报告不足并阻止后续启动。每次打印新的原始证据目录。详见 [运行与恢复手册](release/README.md)、[仓库地图](docs/repository-map.md)和[证据规则](evidence/README.md)。

## 文档入口

| 文档 | 内容 |
| --- | --- |
| [课题完整核心要求](01-course-core-requirements.md) | 课程到底要求完成什么、选题门槛、共同能力要求、阶段交付、对抗组职责、评价 Agent、评分口径及章节作业区别 |
| [P3 选题与全流程执行手册](02-p3-project-proposal.md) | 具体选题、首版范围、六项检查、架构、验收矩阵、分工、每步动作与记录、对照实验、Change、对抗及记录模板 |

## 已确定的选题

**本地教学文档服务的授权边界测试与证据复核 Agent——固定流程与证据驱动调度的对照实验。**

首版围绕一个本地教学文档服务、两名虚构用户、两份文档及附件、六项注册检查展开。先完成模拟器与独立控制器，再接入获批准的本地执行环境；比较固定流程与模型动态调度，并完成运行中撤权、受控对抗、证据复核和恢复交接。

## 当前状态

- 已选定 P3 方向，并整理完整的开题与执行方案。
- v0.1 已实现离线固定调度、注册控制器、六项模拟检查、三类结论与证据落盘；本次自动验证以提交包和原始日志为准。
- 模型动态调度、真实服务、正式对照实验、评价器校准、运行中撤权及独立伙伴验收尚未完成；长版方案中的演练示例不是实测结果。
- 课件要求、课件中的建议，以及本项目新增设计分别标明；正式题目开放范围、授权、截止日期和评分规则以教师确认为准。
- 两人一组、两组结对；每个人都承担实现和验证工作。

建议先读第一份文档的共同要求，再按第二份文档的一页开题卡和步骤表推进。后续规格、代码及原始证据应使用稳定版本和验收 ID 关联。

文档整理日期：2026-10-13。来源为用户提供的四份课程 PPT，完整文件名和页码见文档末尾。

## 参与贡献

本仓库已公开，欢迎通过 Issue 讨论，或 Fork 后提交 Pull Request。具体操作与项目约定见 [贡献说明](CONTRIBUTING.md)。
