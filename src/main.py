#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import getopt
import sys
import time


def get_char():
    """跨平台获取单个字符，无需回车"""
    try:
        #windows
        import msvcrt
        return msvcrt.getch().deecode()
    except ImportError:
        #linux
        import tty,termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    
def immediate_echo():
    """立即回显"""
    print("start to input(press Enter to finish):")
    result = ""
    while True:
        char = get_char()

        if char == "\r" or char == "\n":
            print()
            break

        if char == "\b" or char == "\x7f": 
            if result:
                result = result[:-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()
            continue

        result += char

        time.sleep(0.1)
        
        sys.stdout.write(char)
        sys.stdout.flush()

    return result


def main():
    print("Hello, World!")

    opts,args = getopt.getopt(sys.argv[1:],"hvo:p",["help","version","output=","path="])
    for opt, arg in opts:
        if opt in ("-h","--help"):
            print("Help: This is a help message.")
        elif opt in ("-v","version"):
            print("Version: ")
        elif opt in ("-o","--output"):
            print(f"Output: {arg}")
        elif opt in ("-p","--path"):
            print(f"--Path: {arg}")
        else:
            print("Unknown option")

    usr_input = immediate_echo()
    #print(f"You entered: {usr_input}")

if __name__ == "__main__":
    main()