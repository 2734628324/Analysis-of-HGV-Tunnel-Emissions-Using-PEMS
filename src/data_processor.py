import pandas as pd
import os
# 从 config 模块导入所有文件路径常量
from config import global_config

# 创建一个字典，将简短、易用的别名映射到完整的路径常量
DATASET_MAP = {
    "diesel_g6_01": global_config.HEAVY_DIESEL_G6_01,
    "diesel_g6_01_sw": global_config.HEAVY_DIESEL_G6_01_SW,
    "hgv_n3_g6_01": global_config.HEAVY_HGV_N3_G6_01,
    "hgv_n3_g6_01_test": global_config.HEAVY_HGV_N3_G6_01_TEST,
    "hgv_n3_g6_02": global_config.HEAVY_HGV_N3_G6_02,
    "lng_g6_01": global_config.HEAVY_LNG_G6_01,
}


def load_processed_data(dataset_alias: str) -> pd.DataFrame:
    """
    根据数据集的别名加载对应的 CSV 文件。

    Args:
        dataset_alias: 数据集在 DATASET_MAP 中定义的简短别名。

    Returns:
        pd.DataFrame: 包含数据的 Pandas DataFrame，如果加载失败则返回空 DataFrame。
    """
    # 1. 查找文件路径
    if dataset_alias not in DATASET_MAP:
        print(f"错误: 别名 '{dataset_alias}' 未定义。可用的别名有: {list(DATASET_MAP.keys())}")
        return pd.DataFrame()

    data_path = DATASET_MAP[dataset_alias]

    # 2. 执行加载操作
    try:
        print(f"--- 正在加载数据集: {dataset_alias} ---")
        
        # 假设数据是 CSV 格式，并且时间戳在第一列
        df = pd.read_csv(data_path, index_col=0, parse_dates=True)
        
        print(f"加载成功！记录数: {len(df)}, 列数: {len(df.columns)}")
        print(f"文件来源: {os.path.basename(data_path)}")
        return df
    
    except FileNotFoundError:
        print(f"错误: 找不到文件。路径: {data_path}")
        return pd.DataFrame()
    except Exception as e:
        print(f"加载数据时发生意外错误: {e}")
        return pd.DataFrame()


def concatenate_datasets(aliases: list) -> pd.DataFrame:
    """
    加载并连接 DATASET_MAP 中指定别名的所有数据集。

    Args:
        aliases: 包含要连接的数据集别名列表。

    Returns:
        pd.DataFrame: 连接后的单个 DataFrame。
    """
    dataframes = []
    print(f"\n--- 开始连接 {len(aliases)} 个数据集 ---")

    for alias in aliases:
        df = load_processed_data(alias)
        if not df.empty:
            # 在连接前添加一个源标记列，方便后续分析区分数据来源
            df['source_file'] = alias
            dataframes.append(df)
            
    if not dataframes:
        print("警告: 没有成功加载任何数据集。")
        return pd.DataFrame()

    # 使用 pd.concat 连接所有 DataFrame
    combined_df = pd.concat(dataframes, axis=0)
    print(f"所有数据集连接完成。总记录数: {len(combined_df)}")
    return combined_df

# ----------------------------------------------------
# 这是一个私有函数，用于在 Notebook 环境中正确导入模块
def _add_project_root_to_path():
    """
    将项目根目录动态添加到 sys.path 中，解决 Notebooks 导入 src 模块的问题。
    """
    import sys
    # 假设 Notebook 在 notebooks/ 目录下，向上两级就是项目根目录
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
        print(f"项目根目录已添加到路径: {project_root}")
    else:
        # print("项目根目录已在路径中。")
        pass


# ----------------------------------------------------
# 这是一个用于测试或首次运行的示例函数
# def run_example_load():
#     # 示例: 加载单个文件
#     df_single = load_processed_data("diesel_g6_01")
    
#     # 示例: 连接多个文件
#     all_hgv_data = concatenate_datasets(["hgv_n3_g6_01", "hgv_n3_g6_02", "diesel_g6_01"])
# ----------------------------------------------------
