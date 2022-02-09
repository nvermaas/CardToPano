import argparse
import os
from PIL import Image, ImageDraw, ImageFont

ASPECT_RATIO = 2

def convert_cardboard_to_pano(args):

    # open the file and check whether the source exists)
    print('- open '+args.source_file)
    im = Image.open(args.source_file)

    # determine the dimensions
    print('- size = '+str(im.size))
    width = im.size[0]
    height = im.size[1]
    target_height = round(width / 2)
    vertical_center = round(target_height / 2)
    # this is the vertical position to paste the cardboard image exactly in the middle of the PANO
    vertical_paste_position = round(vertical_center - (height/2))

    # copy the cardboard file to paste it into the new PANO file

    # crop/copy the full image from the cardboard
    box = (0, 0, width, height)
    region = im.crop(box)

    # create a new image with the full PANO dimensions
    #new_color = (128, 128, 128)

    new_size = (width,target_height)
    im_target = Image.new(im.mode,new_size,args.color)

    target_box = (0, vertical_paste_position, width, vertical_paste_position + height)
    im_target.paste(region, target_box)

    # handle the output target file
    source_dir, filename = os.path.split(args.source_file)
    target_filename = "PANO_"+filename

    if args.target_dir:
        # a target_dir is given, store the file there
        target_file = os.path.join(args.target_dir,target_filename)
    else:
        target_file = os.path.join(source_dir, target_filename)


    # play it a little bit safe by not overriding the new file automatically

    print('- save '+target_file)
    #if not os.path.exists(target_file):
        # save the new file
    im_target.save(target_file)
    im_target.show()



    print('ok')

def do_conversion(args):
    # check whether the source exists
    if args.source_file:
        convert_cardboard_to_pano(args)

    # read all files in the directory and convert them
    if args.source_dir:
        pass


def main():
    parser = argparse.ArgumentParser(fromfile_prefix_chars='@')

    parser.add_argument("--source_file",
                        default=None,
                        help="single cardboard file to convert")
    parser.add_argument("--source_dir",
                        default=None,
                        help="directory containing cardboard files to convert")
    parser.add_argument("--target_dir",
                        help="directory to write the converted PANO files to (default is current directory")
    parser.add_argument("--color",
                        default="#C0C0C0",
                        help="Color for the top and bottom bar fill. RGB color in hex format")
    args = args = parser.parse_args()

    print("--- CardToPano (version 9 feb 2022) ---")
    print(args)

    do_conversion(args)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
