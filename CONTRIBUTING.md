# 参与贡献

欢迎通过 Issue 讨论问题，通过 Fork 和 Pull Request（PR）贡献文档、实现和验证。

## 提交流程

1. Fork 本仓库到自己的 GitHub 账号。
2. 克隆自己的 Fork，创建一个描述改动的分支。
3. 完成一个范围清楚的改动，检查文档链接或运行与改动相关的验证。
4. 使用 Git 提交并推送到自己的分支，向本仓库的 `main` 分支提交 PR。
5. 在 PR 中说明问题、改动、验证结果和仍待确认的事项，回应维护者的审查。

```powershell
git clone https://github.com/<你的账号>/ai-native-p3-security-agent.git
cd ai-native-p3-security-agent
git switch -c docs/clarify-requirements
# 编辑并验证改动
git add <改动文件>
git commit -m "docs: clarify course requirements"
git push -u origin docs/clarify-requirements
```

PR 审查通过后由维护者合并。公开仓库允许其他人查看、Fork 和提出 PR；直接向本仓库推送需要维护者单独授予协作者权限。

## 本项目的约定

- 课程共同要求、课件建议、本组设计和教师批准结果应分别标明。
- 修改课程要求时提供源课件文件名及实际幻灯片页码。
- 方案、模拟输出和真实试验结果应明确区分；验收结论引用具体版本和证据。
- 贡献代码时说明如何运行与验证；不要提交密码、Token、真实学生数据或未经授权的目标信息。
- 提交署名使用与自己 GitHub 账号关联的邮箱，或账号提供的 noreply 邮箱。

当前仓库处于选题和方案阶段。欢迎先提出澄清、勘误、范围调整或实施任务建议。
