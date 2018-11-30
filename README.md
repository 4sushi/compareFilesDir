# CompareFilesDir

## Description

Compare files in two directories, print diff for each file. For Linux.

## Python version

Python 2 and Python 3

## Example

### Example 1

Print diff between directory 1 and directory 2. 
* dir1/file1 and dir2/file1 are identical
* dir1/file2.csv and dir2/file2.csv have 1 different line
* file3 exist only in dir2 
```
$ ls -LR test
test:
dir1  dir2  dir3
test/dir1:
file1  file2.csv
test/dir2:
file1  file2.csv  file3
test/dir3:
file1  file2.csv

$ python compare_files_dir.py test/dir1 test/dir2
[1] diff: test/dir1/file3: No such file or directory

[2] Diff finded between 2 files (file2.csv)  
2c2
< 4;5;6
\ No newline at end of file
---
> 7;8;9
\ No newline at end of file
```

Print diff only for csv extension:
```
$ python compare_files_dir.py test/dir1 test/dir2 *.csv 
[1] Diff finded between 2 files (file2.csv)  
2c2
< 4;5;6
\ No newline at end of file
---
> 7;8;9
\ No newline at end of file
```

### Example 2

Print diff between directory 1 and directory 3. Content are identical. 
```
$ python compare_files_dir.py test/dir1 test/dir3
$
```

Here there is no output when the content is identical.