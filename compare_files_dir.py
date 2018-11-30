"""
Compare files in two directories
Print diff for each file
For Linux
"""

import glob
import ntpath
import os
import subprocess
import sys

class colors:
    CYAN = '\x1b[96m'
    BOLD = '\x1b[1m'
    END = '\x1b[0m'
    CYAN_BG_BOLD = CYAN + BOLD


if __name__ == '__main__':
    """
    Input controls
    """
    if len(sys.argv) not in [3,4]:
        print('Error, bad params lenght : python compare_file_dir.py <path_dir_1> <path_dir_2> [extension_file]')
        sys.exit(1)
    dir1 = sys.argv[1]
    dir2 = sys.argv[2]
    if (not os.path.exists(dir1)) or (not os.path.exists(dir2)):
        print('Error, one of the path doesn\'t exist : %s %s' % (dir1, dir2))
        sys.exit(1)
    if len(sys.argv) == 4:
        ext_file = sys.argv[3]
    else:
        ext_file = '*' # '*' for all files type

    """
    Get files name
    """
    # List files
    files1 = glob.glob(os.path.join(dir1, ext_file))
    files2 = glob.glob(os.path.join(dir2, ext_file))
    # Get only file name
    files1 = [ntpath.basename(f) for f in files1]
    files2 = [ntpath.basename(f) for f in files2]
    # Concat and remove duplicate
    files = list(set(files1 + files2))

    """
    Print diff between each file
    """
    cpt = 1
    for f in files:
        s = subprocess.Popen(['diff', os.path.join(dir1, f), os.path.join(dir2, f)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        s.wait()
        stdout, stderr = s.communicate()
        stdout, stderr = stdout.decode('utf-8'), stderr.decode('utf-8')
        # err
        if stderr != '':
            print('%s[%s] %s%s' % (colors.CYAN_BG_BOLD, cpt, stderr, colors.END))
            cpt += 1
        # diff finded
        elif stdout != '':
            print('%s[%s] Diff finded between 2 files (%s) %s \n%s' % (colors.CYAN_BG_BOLD, cpt, f, colors.END, stdout))
            cpt += 1
