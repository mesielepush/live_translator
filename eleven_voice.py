from eleven_voice_utils import *


output_language = 'english'
voice_id = 'VR6AewLTigWG4xSOukaG'

def read_out_load(output_language, voice_id):
    current_file_n = get_current_file_n()
    while True:
        if not os.path.exists(f'transcripts/{str(current_file_n)}.mp3.txt'):
            while_we_wait(current_file_n)
            continue
        else:
            make_mp3(current_file_n, voice_id, output_language)
            current_file_n += 1
            
            
if __name__ == '__main__':
    read_out_load(output_language, voice_id)