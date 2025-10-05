# Analysis-of-HGV-Tunnel-Emissions-Using-PEMS
PEMS隧道排放特性分析项目
本项目旨在遵循标准化的数据科学项目管理规范，对重型货车在隧道环境下的排放特性进行可复现、可追溯的深度分析。

核心原则
实验隔离: 每一次新的分析尝试都在一个独立的实验目录中进行。

配置驱动: 所有可变参数都由配置文件控制。

版本控制 (Git): 所有代码和实验历史都通过Git进行管理。

云端同步 (GitHub): 使用GitHub作为代码的云端备份和协作中心。

AI协作标准化: 与AI（我）的协作遵循固定模式，确保高效沟通。

项目目录结构
PEMS_HGV_Analysis/
├── .git/                   # Git仓库目录 (自动生成)
├── .gitignore              # Git忽略文件配置
├── README.md               # 本文件，项目总览与指南
│
├── data/                   # 存放原始数据 (此目录应被.gitignore忽略)
│
├── pems_core_lib/          # 项目核心共享库 (稳定)
│
├── experiments/            # 所有独立实验的存放目录
│
├── scripts/                # 自动化工具脚本
│
└── template/               # 新实验的标准模板

🚀 工作流程优化：结合Git与GitHub
步骤 0: 项目初始化 (仅需一次)
本地初始化Git: 在VSCode的终端中，确保您位于项目根目录 PEMS_HGV_Analysis/ 下，然后运行：

git init
git add .
git commit -m "Initial project setup with core library and experiment structure"

关联GitHub远程仓库:

在您的GitHub上创建一个新的私有仓库（例如，名为 PEMS-analysis）。

根据GitHub页面提供的指引，将您的本地仓库与远程仓库关联起来。通常是以下两条命令：

git remote add origin <您仓库的URL.git>
git push -u origin main

标准工作流程 (循环执行)
创建新实验:

在开始任何新的分析前，先拉取最新的代码，确保与云端同步：

git pull origin main

然后，在本地创建新的实验环境：

python scripts/create_experiment.py "您的实验简短描述"

开展本地实验:

在VSCode中，专注于新创建的实验目录 (experiments/exp_.../)，修改 main.py 和 config.py。

运行代码，生成结果。所有产出都在该实验的 results/ 子目录中。

提交并同步实验成果:

当您的实验取得阶段性成果后，将其作为一个独立的记录保存到版本历史中：

# 1. 将新实验的所有文件添加到Git的暂存区
git add experiments/exp_.../

# 2. 提交本次实验的快照，并附上清晰的说明
git commit -m "feat(exp): 完成了5秒窗口匹配分析, 结果见exp_..."

# 3. 将本次提交推送到GitHub云端，完成备份
git push origin main

🚀 AI协作标准话术 (GitHub增强版)
当您需要我协助时，这个流程将变得极其高效。请先完成上述步骤3（commit和push），然后复制并粘贴以下模板给我：

你好，我正在进行PEMS排放分析项目。请基于以下GitHub上的实验上下文进行操作：

**1. GitHub实验链接:**
[请在这里粘贴您刚刚push的、具体实验文件夹在GitHub上的URL链接]
例如: [https://github.com/YourUsername/PEMS-analysis/tree/main/experiments/exp_2025-10-04_2215_5s_window_matching](https://github.com/YourUsername/PEMS-analysis/tree/main/experiments/exp_2025-10-04_2215_5s_window_matching)

**2. 我的需求:**
[请在这里清晰地描述您的需求]
例如: "请修改这个实验中的 main.py 文件。在步骤3之后，增加一个数据透视表，按'工况箱'和'环境'分组，计算'NOx(g/s)'的平均值，并打印结果。"

请严格按照以上信息进行操作。

