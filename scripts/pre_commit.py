import json
import subprocess
import sys
import io

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# # Run the git diff command to get the changed files
# result = subprocess.run(["git", "diff", "--name-only", "--cached"], capture_output=True, text=True)
# changed_files = result.stdout.splitlines()

# # Determine the commit type based on the changed files
# commit_type = None
# for file in changed_files:
#     if file.startswith("原理图符号"):
#         commit_type = "原理图符号"
#         break
#     elif file.startswith("PCB封装"):
#         commit_type = "PCB封装"
#         break
# Add more conditions here for other commit types...

# If we couldn't determine the commit type, ask the user
# if commit_type is None:
commit_type = input("无法确定提交类型，请输入提交类型：")

# Ask the user for the commit description
description = input("请输入提交描述：")

# Create the commit message
commit_message = json.dumps({
    "type": commit_type,
    "description": description,
})

# Set the commit message
print(commit_message)
# subprocess.run(["git", "commit", "-m", commit_message])