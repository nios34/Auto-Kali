# -*- coding=UTF8 -*-

import time

from termcolor import *


def main():
    print (colored(
"""
│ Update │ 更新Auto-kali  │
""","bule"))
    XX = input(colored("选项:","yellow"))
    if XX == "Update":
        f = open("/usr/share/auto-kali/Auto-kali-path.conf")
        p = f.read()
        p = str(p)
        p = p.strip()
        os.system("cd %s && git stash && git pull" % p)
        print (colored("操作完成，3秒后重启脚本","blue"))
        time.sleep(3)
        os.system("auto-kali")
        exit
    else:
        main()
        pass
    pass

if __name__ == '__main__':
    main()