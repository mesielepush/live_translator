import subprocess




def main():
    print('start')
    subprocess.Popen(["python", "recorder.py"])
    print('recording...')
    subprocess.Popen(["python", "transcriber.py"])
    print('transcriber on...')
    
if __name__ == "__main__":
    main()