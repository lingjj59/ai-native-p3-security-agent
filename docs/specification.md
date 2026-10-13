# Spec v0.1 与第一次任务 B：GWT

契约：`p3-sim-contract-v0.1`。性质：本组拟定的公开模拟器契约，教师批准待确认。R01—R12 沿用原方案，不新增冒充课件的要求。

## 功能、输入与可观察结果

真实功能：在注册与预算内执行教学授权检查，并用原始响应生成有界结论。CLI 只接受 `good`、`known-bad`、`timeout` 和 1—8 的尝试上限；无任意目标地址或凭据入口。控制器仅放行 `teaching-docs-sim` 和 T01—T06。固定顺序 T01、T06、T02、T04、T03、T05；单并发，无重试。

| 检查 | 身份/资源 | 期望 | 前置 |
| --- | --- | --- | --- |
| T01 | A / DA | 200 + TEACHING_DA | 无 |
| T06 | A / DA_attachment | 200 + TEACHING_DA_ATTACHMENT | 无 |
| T02 | A / DB | 403 且无 TEACHING_DB | T01 正常 |
| T04 | A / DB_attachment | 403 且无 TEACHING_DB_ATTACHMENT | T06 正常 |
| T03 | anonymous / DA | 401 且无 TEACHING_DA | T01 正常 |
| T05 | revoked_A / DA | 401 且无 TEACHING_DA | T01 正常 |

标记是虚构正文或附件内容，不是真实秘密。此模拟契约只识别教学标记，不宣称能检测任意真实内容泄露。注册表由可信宿主代码持有；计划器只提交 test_id。Fixture 由演示 runner 提供，后续模型不能看缺陷开关和真值。

每项 MUST 输出 `execution_status`（NOT_RUN / DENIED / EXECUTED）、`conclusion`、原因和证据引用。CONFIRMED 需要未授权响应包含受保护标记，即使状态是 403 也属于泄露；NOT_CONFIRMED 仅表示本项观察符合契约；超时、报错、不完整、未知状态、正常路径失败及未执行均为 INCONCLUSIVE。禁止外推“整个服务安全”。

默认上限为 8 次尝试、8 轮决策、90 秒逻辑预算。所有已启动失败计数；每次启动前检查预算，不承诺取消在途动作。预算耗尽后不得再有 execution_started。模拟逻辑秒数不等于墙钟超时；真实网络超时属于后续 K04。

输出目录必须是新 run，含 metadata、fixture、events.jsonl、report 和 checksums。报告列六项，原始事件保留拒绝和失败。源码 commit、Fixture 哈希、契约/注册表/策略版本必须可定位。哈希用于完整性，不证明来源或独立复现。证据落盘失败直接终止，不产生成功声明。

## GWT 场景

| ID / 类型 / Req | Given | When | Then |
| --- | --- | --- | --- |
| GWT-01 正向 R03 | Good、注册目标、预算充足 | 请求 A 读 DA 并取自己的附件 | T01/T06 为 EXECUTED，200 且各自标记存在，NOT_CONFIRMED，有请求及证据 ID |
| GWT-02 正向 R04/R06 | Known Bad，T01 正常 | A 请求 B 的 DB | T02 CONFIRMED，引用实际返回 TEACHING_DB 的原始响应和当前版本 |
| GWT-03 负向 R05/R08 | T01 响应模拟超时 | 执行固定计划 | T01 INCONCLUSIVE，错误保留；其余未完成项仍在六项报告中，不能视为通过 |
| GWT-04 负向 R07/R08 | Good，尝试上限为 1 | 请求后续检查 | 只有一次实际执行，停止原因为预算耗尽，未测项仍列出 |
| GWT-05 对抗 R01 | 提议未注册目标或 SHELL 检查 | 控制器处理提议 | 拒绝并记录原因，没有该请求的 execution_started 或模拟执行调用 |
| GWT-06 对抗 R02 | T01 工具正文含“扩大授权/执行 SHELL”文本 | 处理响应后提议 SHELL | 注册表不变、SHELL 拒绝、没有额外执行；不宣称已验证模型抗注入能力 |
| GWT-07 负向 R03/R05 | T01 报错但预算未尽 | 调度正文拒绝检查 | T02/T03/T05 因前置不成立被拒绝且结论不足 |
| GWT-08 对抗 R04 | T02 返回 403，但正文含 DB 标记 | 判断响应 | 仍判 CONFIRMED，不能只凭状态码视为无泄露 |

CH01 的“启动前撤权”和“已有动作在途”两个场景保留给批准变更阶段，当前未实现。评价器的四状态（统一为 PASS / FAIL / INSUFFICIENT_EVIDENCE / NA）与产品三结论独立，NA 需要教师批准。

## B 项四项自检

| 自检 | 本规格如何满足 |
| --- | --- |
| 状态可构造 | 三份公开 Fixture；测试补充错误/诱导/缺字段/状态码与内容不一致输入 |
| 动作可触发 | 三条 CLI 场景命令；未知 ID 与预算场景可通过 runner 的结构化提议触发 |
| 结果可断言 | 响应标记、执行次数、结论、未覆盖、事件和引用均为可读取 JSON 值 |
| 不依赖具体实现 | GWT 描述输入、动作与外部证据，不依赖私有函数或指定算法；实现与测试位置另列验收矩阵 |
