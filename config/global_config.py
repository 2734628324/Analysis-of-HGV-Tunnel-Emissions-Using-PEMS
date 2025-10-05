import os
from pathlib import Path

# 动态获取项目根目录，以支持相对路径
# 假设此文件位于 PEMS_HGV_Analysis/config/global_config.py
try:
    # 使用 __file__ 确定当前文件的绝对路径，并向上跳转两次到项目根目录
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
except NameError:
    # 针对 Notebook 或其他运行环境的回退机制
    PROJECT_ROOT = Path(os.getcwd())

# --- 数据路径 ---
DATA_DIR = PROJECT_ROOT / 'data' 
PROCESSED_DATA_DIR = DATA_DIR / '01_processed' # 你的文件都在这个目录下
RAW_DATA_DIR = DATA_DIR / '01_raw'

# 以下路径是基于你上传的旧 config.py 中使用的文件名来定义的
DIESEL_RAW_DATA_FILE_PATH = PROCESSED_DATA_DIR / 'Heavy_Diesel_G6_01_processed.csv'
DIESEL_SEGMENTS_FILE_PATH = RAW_DATA_DIR / 'segments.xlsx'
LNG_RAW_DATA_FILE_PATH = PROCESSED_DATA_DIR / 'Heavy_LNG_G6_01_processed.csv'
LNG_SEGMENTS_FILE_PATH = DATA_DIR / 'segments_lng.xlsx'

# --- 输出路径 ---
PLOTS_DIR = PROJECT_ROOT / 'results' / 'figures'
PLOTS_DIR.mkdir(parents=True, exist_ok=True) 