import os
import shutil
def copy_directory(src,dst,relative_path = ""):
    for content in os.listdir(src):
        src_path = os.path.join(src, content)
        rel = os.path.join(relative_path, content) if relative_path else content
        dst_path = os.path.join(dst, rel)

        if os.path.isfile(src_path):
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            shutil.copy2(src_path, dst_path)
        elif os.path.isdir(src_path):
            os.makedirs(dst_path, exist_ok=True)
            copy_directory(src_path, dst, rel)
            