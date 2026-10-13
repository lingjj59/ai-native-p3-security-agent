# v0.1 模拟基线：运行、停止与恢复

需要 Git 与 Python 3.11+。无需模型密钥、pip 安装、Docker、管理员权限或网络靶场。首次 clone 需要 GitHub 网络访问，之后程序运行不需要网络。

```text
git clone https://github.com/lingjj59/ai-native-p3-security-agent.git
cd ai-native-p3-security-agent
git switch feat/first-submission
python --version
python -m unittest discover -s eval -v
python scripts/check_docs.py
python scripts/run_demo.py --scenario good
python scripts/run_demo.py --scenario known-bad
python scripts/run_demo.py --scenario timeout
python scripts/run_demo.py --scenario good --max-attempts 1
```

PR 合并后可使用 main；复现本次原始证据时，优先 `git switch --detach <manifest 中的 source_commit>` 在另一个干净 clone 中运行，避免覆盖本地未提交工作。

命令打印新 run 的绝对路径。Good：6 次执行，各项 NOT_CONFIRMED；Known Bad：T02 CONFIRMED 且原始响应含 DB 标记；Timeout：1 次执行，T01 INCONCLUSIVE，预算耗尽，所有六项均没有有效覆盖。尝试预算 1：只启动 T01，后续项仍保留。状态码/响应事件在 events.jsonl，摘要在 report.json。

**停止**：程序是短时 CLI，无后台服务或端口，Ctrl+C 可中断。程序异常退出或缺 report/checksums 则视为未完成，不作为通过。异常证据目录保留供诊断。

**重置**：每次启动自动建立新的模拟器、控制器和 UUID 目录，用户/文档全在内存；无需删除旧 run。若需要临时试验，使用 `--output <新的临时目录>`。清理时仅人工删除自己确认的未提交临时 run，不用全目录递归清理命令。

**恢复**：记录最后验证 commit，在新目录 clone/checkout 对应 commit，重新运行测试及三场景。历史报告不就地续写，新的结果使用新 run ID。本次不修改数据库或外部目标，因此没有数据迁移/外部回滚。

**限制**：没有真实 HTTP 服务、模型动态计划器、独立评价器、K1—K6 校准、CH01 实时撤权或伙伴复现。只有逻辑预算，不能证明网络墙钟超时/在途取消。Fixture 中的超时是真实执行的模拟分支，不能标成真实网络超时测量。证据写入失败终止，但尚无电源故障/持久化事务保证。完整学期验收仍以矩阵中的未完成项为准。
