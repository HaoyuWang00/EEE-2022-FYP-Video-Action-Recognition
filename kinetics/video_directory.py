import os
import shutil

# path to the raw videos
dataset_path = '/home/students/s121md105_01/kinetics-dataset/k400'
output_frame_path = '/home/students/s121md105_01/kinetics-dataset/k400_struct_vid'
label_path = '/home/students/s121md105_01/kinetics-dataset/k400/annotations'
kinetics_label_map_path = '/home/students/s121md105_01/temporal-shift-module/tools/kinetics_label_map.txt'

if __name__ == '__main__':
    with open(kinetics_label_map_path) as f:
        categories = f.readlines()
        categories = [c.strip().replace(' ', '_').replace('"', '').replace('(', '').replace(')', '').replace("'", '') for c in categories]
    assert len(set(categories)) == 400
    # class-index pairs
    dict_categories = {}
    for i, category in enumerate(categories):
        dict_categories[category] = i
    # print(dict_categories)


    # for val/test/train
    directories_input = ['val', 'test', 'train']
    files_input = ['val.csv', 'test.csv', 'train.csv']
    for (direcotry_input, filename_input) in zip(directories_input, files_input):
        output_frame_path_split = os.path.join(output_frame_path, direcotry_input)
        # specify train/test/val split
        vid_folder_path = os.path.join(dataset_path, direcotry_input)
        # class-count pairs
        count_cat = {k: 0 for k in dict_categories.keys()}
        with open(os.path.join(label_path, filename_input)) as f:
            lines = f.readlines()[1:]
        # video names
        folders = []
        # ordered indexes that are corespondent to categories_list
        idx_categories = []
        # ordered class names extracted from the annotation file
        categories_list = []
        for line in lines:
            line = line.rstrip()
            items = line.split(',')
            folders.append(items[1])
            this_catergory = items[0].replace(' ', '_').replace('"', '').replace('(', '').replace(')', '').replace("'", '')
            categories_list.append(this_catergory)
            idx_categories.append(dict_categories[this_catergory])
            count_cat[this_catergory] += 1
        print(max(count_cat.values()))

        assert len(idx_categories) == len(folders)

        video_list = os.listdir(vid_folder_path)
        for vid_file_path in video_list:
            # trunk the name
            # 9_00t9hFaZ4_000053_000063.mp4
            # vid_code = vid_file_path.split('_00')[0]
            vid_code = vid_file_path[:11]
            idx = folders.index(vid_code)
            cat_idx = idx_categories[idx]
            cat_name = list(dict_categories.keys())[list(dict_categories.values()).index(cat_idx)]
            # vid_class = 
            cat_folder_path = os.path.join(output_frame_path_split, cat_name)

            # dataset_path/sled_dog_racing/zzokQ8DKETs_112
            # if this folder exists
            if not os.path.exists(cat_folder_path):
                os.mkdir(cat_folder_path)
            # move the video
            print('Moving ' + vid_file_path + ' to ' + cat_folder_path)
            original_path = os.path.join(vid_folder_path, vid_file_path)
            destination_path = cat_folder_path
            # print(1)
            shutil.move(original_path, destination_path)