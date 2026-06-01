import platform
import sys

os_name = platform.system()

python_version = sys.version

output_string = f"OS info is {os_name} Python version is {python_version}"

with open('os_info.txt', 'w', encoding='utf-8') as file:
    file.write(output_string)

print(f"Информация записана в файл 'os_info.txt':\n{output_string}")
