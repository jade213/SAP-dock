import subprocess

'''
open putty - y
launch ssh - y
'''
def open_putty():
    #subprocess.call('start cmd', shell=True)
    #subprocess.run('putty', shell=True)
    subprocess.Popen(['C:\\Users\jadec\Downloads\puTTY\putty.exe', '-ssh', 'unix.ncl.ac.uk'], bufsize=0)


def main():
    open_putty()

if __name__ == '__main__':
    main()
