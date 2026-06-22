import os
from huggingface_hub import hf_hub_download




VGG_PATH = "code/vgg_normalised.pth"
DECODER_DIR = "code/experiment/final_exp"
DECODER_PATH = os.path.join(DECODER_DIR, "decoder_final.pth")
REPO_ID= "isushmeeta/modelnst"

#GDrive file IDs

def download():
    #download VGG
    if not os.path.exists(VGG_PATH):
        print("Downloading vgg_normalised.pth...")
        os.makedirs("code", exist_ok=True)
        hf_hub_download(repo_id=REPO_ID,filename="vgg_normalised.pth", local_dir="code")
        print(" vgg_normalised.pth downloaded!")
    else:
        print(" vgg_normalised.pth already exists, skipping.")

    #download Decoder
    if not os.path.exists(DECODER_PATH):
        print("Downloading decoder_final.pth...")
        os.makedirs(DECODER_DIR, exist_ok=True)
        hf_hub_download(repo_id=REPO_ID, filename="decoder_final.pth", local_dir=DECODER_DIR)
        print("decoder_final.pth downloaded!")
    else:
        print("decoder_final.pth already exists, skipping.")

if __name__ == "__main__":
    download()
