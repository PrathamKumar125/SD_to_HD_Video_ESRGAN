# SD_to_HD_Video_ESRGAN

---

This repository contains scripts and instructions to upscale a video using ESRGAN (Enhanced Super-Resolution Generative Adversarial Networks).

## Steps to Upscale Video:

### 1. Clone Repository
Clone the ESRGAN repository to your local machine:

```
git clone https://github.com/xinntao/ESRGAN ESRGAN_folder
```

Replace `ESRGAN_folder` with your desired directory name.

### 2. Download Model
Download the ESRGAN model checkpoint from Google Drive and place it into the cloned repository. [Link to Model](https://drive.google.com/drive/u/0/folders/17VYV_SoZZesU6mbxz2dMAIccSSlqLecy)

### 3. Install Dependencies
Navigate to the cloned repository directory and install dependencies:

```
pip install -r requirements.txt
```

### 4. Convert Video into SD Frames
Run `ingest.py` to convert your video into SD frames:

```
python ingest.py
```

### 5. Convert Frames into HD Frames using ESRGAN Model
Use the ESRGAN model to enhance SD frames to HD quality:

```
python ESRGAN_folder/test.py
```

### 6. Convert HD Frames to an HD Video
Assemble the enhanced HD frames back into an HD video:

```
python assemble.py
```


Adjust the paths and commands as per your specific setup. Include any additional details or troubleshooting steps that might be helpful for users. This README.md format provides a clear and structured guide for users to follow when using your repository for video upscaling with ESRGAN.
