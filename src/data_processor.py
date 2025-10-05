import pandas as pd
from pathlib import Path
# 导入整个 config.global_config 模块
from config import global_config

def load_processed_data(file_name: str) -> pd.DataFrame:
    """
    从 data/01_processed/ 目录加载一个处理过的数据文件。
    这个函数现在直接接收文件名，不再使用别名系统。

    参数:
    file_name (str): 要加载的文件名 (例如 'Heavy_Diesel_G6_01_processed.csv').

    返回:
    pd.DataFrame: 加载后的数据。
    
    异常:
    FileNotFoundError: 如果在指定目录下找不到文件。
    """
    # 使用 global_config 模块中的路径常量来构建完整路径
    file_path = global_config.PROCESSED_DATA_DIR / file_name
    
    if not file_path.exists():
        raise FileNotFoundError(f"错误：在指定路径找不到文件: {file_path.resolve()}")
    
    df = pd.read_csv(file_path)
    print(f"成功加载文件: {file_name}")
    return df

