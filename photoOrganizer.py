#! /usr/bin/env python3
#! photoOrganizer.py - A program that walks through a directory, sorting
#  photos in to folders based on date created

import os,time,shutil

def organizePhotos(targetFolder):
    for folder,subfolders,files in os.walk(targetFolder):
        for file in files:
            year = time.ctime(os.path.getmtime(os.path.join(folder,file))).split()[4]
            month = time.ctime(os.path.getmtime(os.path.join(folder,file))).split()[1]
            if not os.path.exists(os.path.join(targetFolder,year)):
                os.mkdir(os.path.join(targetFolder,year))
            if not os.path.exists(os.path.join(targetFolder,year,month)):
                os.mkdir(os.path.join(targetFolder,year,month))
            print(f'Copying file {file}...')
            shutil.move(os.path.join(folder,file),os.path.join(targetFolder,year,month,file))
    print('Done.')
organizePhotos('/users/neilbarry/desktop/phototest')
