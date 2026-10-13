# 影响分析

基线为 `91ece8d` 的纯文档仓库；无既有业务库、接口、数据库或迁移负担。本次新增离线 Python 包、Fixture、测试、CI、开题材料和证据；原两份长文保持课程来源，更新 README 导航与阶段状态。

| 变化 | 影响 | 验证 / 恢复 |
| --- | --- | --- |
| 注册检查/响应契约 | controller、executor、reporting、Fixture、GWT | 同步契约版本，运行所有单元检查 |
| 预算/前置 | 启动数量、未覆盖与停止理由 | budget/prerequisite/timeout 测试 |
| 证据字段 | 复核脚本、索引、未来 evaluator | 引用存在性、哈希与版本记录 |
| 文档导航 | AGENTS、README、提交入口 | check_docs 相对链接检查 |
| 后续 CH01 | 授权源、队列、事件、报告、状态及测试 | 批准后新增变更契约，保存旧失败，不覆盖旧证据 |

恢复采用单独目录 checkout 已提交版本重新运行，不 reset 用户工作区，不删除历史提交与原始运行。首次证据绑定实现 commit；后续仅增加证据的 commit 不改变该历史源码绑定。
