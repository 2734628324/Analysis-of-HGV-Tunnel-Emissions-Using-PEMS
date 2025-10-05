import os
import sys

# 定义要忽略的文件夹和文件（例如 Git 文件夹、Python 缓存、数据结果）
IGNORE_DIRS = ['.git', '__pycache__', 'results', 'venv', '.ipynb_checkpoints']
IGNORE_FILES = ['.DS_Store', 'print_tree.py'] # 忽略脚本自身

def print_directory_tree(start_dir):
    """
    递归打印项目目录结构。
    """
    print(f"项目根目录: {start_dir}")
    for root, dirs, files in os.walk(start_dir, topdown=True):
        
        # 排除在 IGNORE_DIRS 列表中的目录
        # 注意：必须原地修改 dirs 列表，os.walk 才会跳过这些目录
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        # 计算当前层级深度，并生成前缀
        level = root.replace(start_dir, '').count(os.sep)
        indent = '│   ' * level
        
        # 打印当前目录名 (如果不是根目录)
        if level > 0:
            dir_name = os.path.basename(root)
            print(f"{indent[:-4]}└── {dir_name}/")
        
        # 打印文件
        sub_indent = '│   ' * (level + 1)
        
        # 过滤要忽略的文件
        files = [f for f in files if f not in IGNORE_FILES]
        
        for f in files:
            print(f"{sub_indent[:-4]}└── {f}")

if __name__ == "__main__":
    # 假设脚本在项目根目录运行
    project_root = os.path.abspath('.')
    
    # 将项目根目录添加到系统路径，以确保脚本能找到
    if project_root not in sys.path:
        sys.path.append(project_root)
        
    print_directory_tree(project_root)
