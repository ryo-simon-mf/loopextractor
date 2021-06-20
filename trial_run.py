import os
import argparse
import loopextractor

parser = argparse.ArgumentParser(description='To Run loopextractor easier')
parser.add_argument('--input_audio_file', type=str)
parser.add_argument('--n_template', type=list, default=[30,25,10])
parser.add_argument('--output_audio_file', type=str)
args = parser.parse_args()

#print(args.input_audio_file)
#print(args.output_audio_file)
#print(args.n_template)


# make output directory if it isn't exit
tar_dir_name = './' + args.output_audio_file
try:
    os.mkdir(tar_dir_name)
except FileExistsError:
    ask1 = input("This folder(directory) already exists. Do you wanna overwrite?(yes/no)")
    if(ask1 == 'yes'):
        print('Over write' + args.output_audio_file)
        os.makedirs(tar_dir_name, exist_ok=True)
    elif(ask1 == 'no'):
        print('End this task.')
        exit()


# run loopextracktor
loopextractor.run_algorithm(args.input_audio_file, n_templates=[30,25,10], output_savename= './' + args.output_audio_file + '/' + args.output_audio_file)


print('Finished this task')
