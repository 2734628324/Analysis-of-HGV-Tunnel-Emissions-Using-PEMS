# Analysis-of-HGV-Tunnel-Emissions-Using-PEMS  
## PEMS隧道排放特性分析项目

本项目旨在遵循标准化的数据科学项目管理规范，对重型货车在隧道环境下的排放特性进行可复现、可追溯的深度分析。

---

### 核心原则
1. **实验隔离**  
   每一次新的分析尝试都在一个独立的实验目录中进行。

2. **配置驱动**  
   所有可变参数都由配置文件控制。

3. **版本控制 (Git)**  
   所有代码和实验历史都通过 Git 进行管理。

4. **云端同步 (GitHub)**  
   使用 GitHub 作为代码的云端备份和协作中心。

5. **AI 协作标准化**  
   与 AI（我）的协作遵循固定模式，确保高效沟通。

---

### 项目目录结构
项目根目录: D:\A-Code\PEMS_HGV_Analysis
└── .gitignore
└── README.md
└── config/
│   └── analysis_params.yaml
│   └── global_config.py
└── data/
│   └── 01_processed/
│   │   └── Heavy_Diesel_G6_01_processed.csv
│   │   └── Heavy_Diesel_G6_01_Software_processed.csv
│   │   └── Heavy_HGV_N3_G6_01_processed.csv
│   │   └── Heavy_HGV_N3_G6_01_test_processed.csv
│   │   └── Heavy_HGV_N3_G6_02_processed.csv
│   │   └── Heavy_LNG_G6_01_processed.csv
│   └── 01_raw/
│   │   └── 20210529-LDGV国六1.xlsx
│   │   └── 20230407-PHEV国六1.xlsx
│   │   └── 20250226-HGV_N3国六b01_1Hz.csv
│   │   └── 20250316-HGV_N3国六b02 _1Hz.csv
│   │   └── 20250807-重柴国六1_1Hz.csv
│   │   └── 20250807-重柴国六1_1Hz.pdf
│   │   └── 20250807-重柴国六1_1Hz.xlsx
│   │   └── 20250807-重柴国六1_cleaned.csv
│   │   └── 20250808-LNG01_1Hz.csv
│   │   └── 20250808-LNG01_1Hz_已处理.csv
│   │   └── 交叉口时间表.xlsx
│   │   └── 国六LNG_隧道时间与分类_segments.xlsx
│   │   └── 国六柴油_隧道时间与分类_segments.xlsx
└── notebooks/
│   └── 01_initial_eda.ipynb
└── src/
│   └── data_processor.py
│   └── model_trainer.py
│   └── __init__.py

