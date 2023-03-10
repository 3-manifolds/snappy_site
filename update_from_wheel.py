import sys
import os
import shutil
import zipfile

work_dir = 'docs-extract-scratch'
wheel_contents = zipfile.ZipFile(sys.argv[1])
if os.path.exists(work_dir):
    shutil.rmtree(work_dir)

for file_name in wheel_contents.namelist():
    if file_name.startswith('snappy/doc'):
        wheel_contents.extract(file_name, work_dir)

keepers = ['CNAME', '.nojekyll']
for file_name in keepers:
    os.rename('docs/' + file_name, work_dir + '/snappy/doc/' + file_name)

shutil.rmtree('docs')
os.rename('docs-extract-scratch/snappy/doc', 'docs')
shutil.rmtree('docs-extract-scratch')
