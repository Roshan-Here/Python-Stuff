#  install rembg & pillow using pip || may need to download additional packages while running.
from rembg import remove
from PIL import Image
from pathlib import Path
import os,time

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
INPUT_PATH = os.path.join(BASE_DIR,r'Adv\sampledata\SampleData.jpg')
OUTPUT_PATH = os.path.join(BASE_DIR,r'Adv\sampledata\SampleData.png')
# print(INPUT_PATH)
# print(OUTPUT_PATH)
# input_path = r'./sampledata/SampleData.jpg'

print('READING INPUT ....')
try:
    inp = Image.open(INPUT_PATH)
    time.sleep(4)
    output = remove(inp)
    output.save(OUTPUT_PATH)
    time.sleep(3)
    print('Image Background removed sucessfully')
except Exception as e:
    print(f'Some Error occured : {e}')