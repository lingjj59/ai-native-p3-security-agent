# R01—R12 验收矩阵

角色均为拟分工；A1/A2 真实身份与人工签署待登记。本次模拟基线 14 项自动测试通过，运行结果见[首次提交记录](submissions/first-submission.md)，自动检查不等于伙伴复核。

| Req | MUST 与 GWT | 自动检查/未来验收 | 证据路径 | 实现 / 验证 | 当前范围 |
| --- | --- | --- | --- | --- | --- |
| R01 | 未注册目标/动作不执行；05 | test_unknown_target_never_executes / test_unknown_action_never_executes | tests.txt；events.jsonl | A1 / A2 | 模拟实现 |
| R02 | 模型不能扩授权；06 | test_injection_in_response_cannot_expand_registration | tests.txt；注册表快照比对 | A1 / A2 | 确定性门已实现，模型未接入 |
| R03 | 正常路径可用；01/07 | test_good_normal_paths_and_all_six_checks / test_failed_prerequisite_blocks_body_checks | Good report + observation | A2 / A1 | 模拟实现 |
| R04 | 正确确认反例；02/08 | test_known_bad_discloses_db_with_reference / test_denial_status_with_canary_is_still_disclosure | Bad T02 observation | A1 / A2 | 模拟实现 |
| R05 | 工具故障结论不足；03/07 | test_timeout_is_inconclusive_and_consumes_budget / test_missing_body_or_unexpected_status_is_inconclusive | Timeout report + events | A1 / A2 | 模拟实现 |
| R06 | 引用存在、版本匹配且支持 | test_duplicate_not_reexecuted_and_references_exist；未来评价器假引用/版本错配/不支持三类校准 | report + metadata + checksums | A2 / A1 | 生成与存在性检查已实现，完整独立验证待 K06 |
| R07 | 执行层预算停止；04 | test_attempt_budget_keeps_uncovered / test_decision_budget_stops_repeated_invalid_proposals | tests.txt；事件次数 | A1 / A2 | 模拟实现，不含真实墙钟取消 |
| R08 | 六项覆盖保留；03/04 | Good、Timeout、预算测试 | 每份 report.results/uncovered | A1 / A2 | 模拟实现 |
| R09 | 运行与版本关联 | metadata、Fixture 快照及 SHA256 | 每个 run 的 metadata/checksums | A2 / A1 | 模拟元数据已实现，模型字段为空 |
| R10 | 重置/伙伴复现 | 按 release 手册在新环境重跑 | 伙伴运行待提交 | A1 / A2 | 本机可重跑，独立伙伴未完成 |
| R11 | 运行中撤权无新动作 | CH01 两个时点与在途边界回归 | review/changes/，待批准后生成 | A2 / A1 | 未实现 |
| R12 | 四状态评价/校准/签署 | K1—K6、实际交叉报告 | evaluator/、review/，未来记录 | A2 / A1 | 未实现 |

当前测试文件：`eval/test_baseline.py`；命令：`python -m unittest discover -s eval -v`。公开模拟[证据索引](../evidence/manifest.json)已提交，不能据此将整张学期矩阵标成 PASS。
