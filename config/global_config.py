import os
from pathlib import Path

# --- 项目根目录 ---
# 动态获取项目根目录，这是所有路径的基础
try:
    # 适用于 .py 文件：从当前文件位置向上查找
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
except NameError:
    # 适用于 Notebook：从当前工作目录向上查找
    # 假设 Notebook 在 notebooks/ 目录下运行
    PROJECT_ROOT = Path(os.getcwd()).parent if "notebooks" in os.getcwd() else Path(os.getcwd())


# --- 数据路径 ---
DATA_DIR = PROJECT_ROOT / 'data'
PROCESSED_DATA_DIR = DATA_DIR / '01_processed'
RAW_DATA_DIR = DATA_DIR / '01_raw'

# --- 核心文件路径常量 ---
# 定义好之后，项目中任何地方都通过这个变量来引用，保证统一
DIESEL_RAW_DATA_FILE_PATH = PROCESSED_DATA_DIR / 'Heavy_Diesel_G6_01_processed.csv'
DIESEL_SEGMENTS_FILE_PATH = RAW_DATA_DIR / '国六柴油_隧道时间与分类_segments.xlsx'

LNG_RAW_DATA_FILE_PATH = PROCESSED_DATA_DIR / 'Heavy_LNG_G6_01_processed.csv'
LNG_SEGMENTS_FILE_PATH = RAW_DATA_DIR / '国六LNG_隧道时间与分类_segments.xlsx'

# --- 数据输出路径 ---
# 定义处理完成后，带有标签的数据的保存路径
DIESEL_TAGGED_OUTPUT_PATH = PROCESSED_DATA_DIR / 'Heavy_Diesel_G6_01_tagged.csv'
LNG_TAGGED_OUTPUT_PATH = PROCESSED_DATA_DIR / 'Heavy_LNG_G6_01_tagged.csv'


# --- 输出路径 ---
RESULTS_DIR = PROJECT_ROOT / 'results'
PLOTS_DIR = RESULTS_DIR / 'figures'

# 自动创建尚不存在的输出目录
PLOTS_DIR.mkdir(parents=True, exist_ok=True)

