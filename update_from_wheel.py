import sys
import os
import shutil
import zipfile

wheel_contents = zipfile.ZipFile(sys.argv[1])
for dir_name in ['docs', 'docs-extract-scratch']:
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    
for file_name in wheel_contents.namelist():
    if file_name.startswith('snappy/doc'):
        wheel_contents.extract(file_name, 'docs-extract-scratch')

os.rename('docs-extract-scratch/snappy/doc', 'docs')
shutil.rmtree('docs-extract-scratch')

