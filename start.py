import subprocess
import time
import webbrowser
import os

def start_server():
    """直接使用虚拟环境的python.exe"""
    # 虚拟环境的Python解释器路径
    venv_python = r"E:\warn\env\Scripts\python.exe"
    manage_py = r"E:\warn\manage.py"
    
    # 检查文件是否存在
    if not os.path.exists(venv_python):
        print(f"错误：找不到虚拟环境的Python解释器: {venv_python}")
        return
    
    if not os.path.exists(manage_py):
        print(f"错误：找不到manage.py: {manage_py}")
        return
    
    try:
        print("启动Django服务器...")
        
        # 切换到项目目录
        project_dir = r"E:\warn"
        os.chdir(project_dir)
        
        # 使用虚拟环境的Python直接运行
        cmd = f'"{venv_python}" manage.py runserver'
        
        # 在新窗口中启动服务器
        server_process = subprocess.Popen(
            f'cmd /c start cmd /k "{cmd}"',
            shell=True
        )
        
        print("等待服务器启动...")
        time.sleep(1)
        
        print("打开浏览器...")
        webbrowser.open("http://127.0.0.1:8000")
        
        print("完成！")
        
        
        input("\n按Enter键退出启动脚本（服务器将继续运行）...")
        
    except Exception as e:
        print(f"启动失败: {e}")
        input("按Enter键退出...")

if __name__ == "__main__":
    start_server()
