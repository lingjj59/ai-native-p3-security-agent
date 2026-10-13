# 只读评价 Agent：设计占位

当前没有可运行评价器；产品的 `reporting.py` 不是独立评价 Agent。

K06 计划读取冻结契约、清单和原始证据，做确定性索引/版本/引用/计数预检，再一次受限模型判读，输出校验后人工核查。输入白名单不含被评仓库的 AGENTS/Hook 执行权，不继承产品工具。需要复测时交由批准 runner。

输出拟定字段：criterion_id、status、evidence_level、evidence_ids、finding、scope、missing、suggested_check、score_suggestion=null、human_signoff=pending。status 统一为 PASS / FAIL / INSUFFICIENT_EVIDENCE / NA；原长版方案的 NOT_APPLICABLE 在新实现中归一为 NA，且只接受教师预先批准的不适用项。

首轮 Claim：授权边界（R01/R02）；结论与证据（R04—R06）；预算/覆盖/停止（R07/R08）。K1 有效证据、K2 明确反例、K3 只有自述、K4 诱导、K5 虚构 ID/错版本、K6 批准 NA 均须保存实际输出、人工期望、差异与重跑。目前全部 `not_run`，不能提交成校准通过。
