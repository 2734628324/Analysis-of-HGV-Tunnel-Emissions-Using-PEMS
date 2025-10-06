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

def load_segments_data(file_path: Path) -> pd.DataFrame:
    """
    加载路段定义文件 (Excel)。
    """
    if not file_path.exists():
        raise FileNotFoundError(f"错误：在指定路径找不到路段文件: {file_path.resolve()}")
    
    df_segments = pd.read_excel(file_path)
    print(f"成功加载路段定义文件: {file_path.name}")
    return df_segments

def tag_segments(df_raw: pd.DataFrame, df_segments: pd.DataFrame) -> pd.DataFrame:
    """
    根据路段定义，为原始数据打上标签 (例如：隧道、开放道路)。
    """
    print("\n--- 开始为数据打标签 ---")
    df = df_raw.copy()

    # 1. 转换时间格式
    df['时间戳'] = pd.to_datetime(df['时间戳'])
    df_segments['StartTime'] = pd.to_datetime(df_segments['StartTime'])
    df_segments['EndTime'] = pd.to_datetime(df_segments['EndTime'])

    # 2. 创建新列并设置默认值
    df['SegmentName'] = 'OpenRoad'
    df['SegmentType'] = 'OpenRoad'

    # 3. 遍历路段定义并为数据打标签
    # 使用 .iterrows() 效率较低，但对于路段定义这种行数很少的表是完全可以接受的
    for _, row in df_segments.iterrows():
        # 创建一个布尔掩码 (boolean mask) 来选择在时间范围内的数据
        mask = (df['时间戳'] >= row['StartTime']) & (df['时间戳'] <= row['EndTime'])
        # 使用 .loc 更新匹配行的数据
        df.loc[mask, 'SegmentName'] = row['SegmentName']
        df.loc[mask, 'SegmentType'] = row['SegmentType']
    
    print("打标签完成！")
    return df

def clean_emission_data(df: pd.DataFrame, columns: list, floor_value: float = 0.0) -> pd.DataFrame:

    """
    清洗指定的排放数据列，将负值或零值替换为指定的底板值。
    """
    print(f"\n--- 正在清洗排放数据列: {columns} ---")
    df_cleaned = df.copy()
    for col in columns:
        if col in df_cleaned.columns:
            # 计算有多少值需要被校正
            invalid_count = (df_cleaned[col] <= 0).sum()
            if invalid_count > 0:
                print(f"  - 在列 '{col}' 中发现 {invalid_count} 个无效值 (<=0)，将校正为 {floor_value}。")
                # 执行替换
                df_cleaned[col] = df_cleaned[col].apply(lambda x: floor_value if x <= 0 else x)
    print("数据清洗完成！")
    return df_cleaned

def save_tagged_data(df: pd.DataFrame, output_path: Path):
    """
    将处理好的（已打标签的）数据保存到指定路径。
    """
    print(f"\n--- 正在保存已处理的数据 ---")
    try:
        df.to_csv(output_path, index=False, encoding='utf-8-sig')
        print(f"成功将数据保存至: {output_path.resolve()}")
    except Exception as e:
        print(f"保存文件时出错: {e}")




