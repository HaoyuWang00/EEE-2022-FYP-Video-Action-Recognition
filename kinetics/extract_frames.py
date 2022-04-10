import os
import tarfile


dir_name = '/home/students/s121md105_01/EPIC-KITCHENS'
dst_name = '/home/students/s121md105_01/EPIC-KITCHENS-Data'
extension = ".tar"
modality = 'rgb_frames'
id = 'P'

os.chdir(dir_name) # change directory from working dir to dir with files

for item in sorted(os.listdir(dir_name)): # loop through items in dir
    if id in item:
        folder = os.path.join(dir_name, item, modality)
        
        
        for file in sorted(os.listdir(folder)):
            if file.endswith(extension): # check for ".zip" extension
                file_name = os.path.join(folder, file) # get full path of files

                dst_folder = os.path.join(dst_name, item, file[:-4])
                if os.path.exists(dst_folder):
                    pass
                else:
                    os.makedirs(dst_folder)
                print("Extracting " + file_name + " to " + dst_folder)
                tar_ref = tarfile.open(file_name) # create zipfile object
                tar_ref.extractall(dst_folder) # extract file to dir
                tar_ref.close() # close file
                # os.remove(file_name) # delete zipped file

print("**** Extraction Done ****")