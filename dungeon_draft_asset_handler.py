import os
import glob
import json
import argparse

#                       __    __    __    __
#                      /  \  /  \  /  \  /  \
# ____________________/  __\/  __\/  __\/  __\_____________________________
# ___________________/  /__/  /__/  /__/  /________________________________
#                    | / \   / \   / \   / \  \____
#                    |/   \_/   \_/   \_/   \    o \
#                                            \_____/--<   Ssssss...

class SnakeCaseRenamer:

    def __init__(self, path = os.getcwd(), identity = '/**/*.png'):
        self.files = self.get_files(path, identity)

    def to_snake_case(self, string):
        return string.replace(' ', '_').lower()

    def rename(self):
        for file in self.files:
            split_file_dir = os.path.split(file)
            file_name = split_file_dir[1]
            new_name = self.to_snake_case(file_name)
            new_name_dir = os.path.join(split_file_dir[0], new_name)
            print(f"Renaming to {new_name_dir}")
            os.rename(file, new_name_dir)

    def get_files(self, path, identity):
        return glob.glob(path + identity, recursive=True)

#      _                                    
#     | |   ( `U         w        `U )            
#   __| |_   _ _ __   __ _  ___  ___  _ __  
#  / _` | | | | '_ \ / _` |/ _ \/ _ \| '_ \ 
# | (_| | |_| | | | | (_| |  __/ (_) | | | |
#  \__,_|\__,_|_| |_|\__, |\___|\___/|_| |_|
#                     __/ |   D R A F T                 
#                    |___/    A S S E T
#                           H A N D L E R

class DungeonDraftAssetHandler:

    def __init__(self, tag_name = 'MyTag', prepend_text = 'textures/objects/', file_name = 'default', path = os.getcwd(), identity = '/**/*.png'):
        self.prepend_text = prepend_text
        self.file_name = file_name
        self.files_names = self.get_file_names(path, identity) 
        self.assets = {
            "tags": {
                "Colorable": []
            }
        }
        self.assets['tags'][tag_name] = self.files_names

    def write(self):
        out_file = open(self.file_name, 'w')
        json.dump(self.assets, out_file, indent = 2)
        out_file.close()

    def get_file_names(self, path, identity):
        files = glob.glob(path + identity, recursive=True)
        file_names = []

        for file in files:
            split_file_dir = os.path.split(file)
            file_names.append(self.prepend_text + split_file_dir[1])

        return file_names

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

if __name__ == '__main__':

    # Create the parser
    my_parser = argparse.ArgumentParser(description='List the content of a folder', epilog='Paalam :(')

    my_parser.add_argument('-t', '--tag', default='MyTag', type=str, required=False, help='Tag name')
    my_parser.add_argument('-p', '--prependtext', default='textures/objects/', type=str, required=False, help='Prepend file name text')

    args = my_parser.parse_args()

    print(args)

    tag_name = args.tag
    prepend_text = args.prependtext

    renamer = SnakeCaseRenamer()
    renamer.rename()

    asset_handler = DungeonDraftAssetHandler(tag_name, prepend_text)
    asset_handler.write()