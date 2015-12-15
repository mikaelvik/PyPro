# PyPro

Scripts to handle my GoPro movies and photos: 
- renaming based on exif data
- move and copy

## Requirements

Download pip-installer [get-pip.py](https://bootstrap.pypa.io/get-pip.py)

```bash 
# pip, already downloaded
python get-pip.py 

# exifread
sudo -H pip install exifread

# PIL
sudo -H pip install PIL --allow-all-external --allow-unverified PIL

# hachoir
sudo -H pip install hachoir-metadata
sudo -H pip install hachoir
sudo -H pip install hachoir-core
sudo -H pip install hachoir-parser

