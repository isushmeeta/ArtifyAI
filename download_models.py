import os
import gdown


VGG_PATH = "vgg_normalised.pth"
DECODER_DIR = "experiment/final_exp"
DECODER_PATH = os.path.join(DECODER_DIR, "decoder_final.pth")

#GDrive file IDs
VGG_ID = "1S0U2SJLNx6IibdFJ5nfEF53TjStDMnmz"
DECODER_ID = "1cJlQWWSR-QzjzP-m5-OIFnMN5tzLURI8"

def download():
    #download VGG
    if not os.path.exists(VGG_PATH):
        print("Downloading vgg_normalised.pth...")
        gdown.download(id=VGG_ID, output=VGG_PATH, quiet=False)
        print(" vgg_normalised.pth downloaded!")
    else:
        print(" vgg_normalised.pth already exists, skipping.")

    #download Decoder
    if not os.path.exists(DECODER_PATH):
        print("Downloading decoder_final.pth...")
        os.makedirs(DECODER_DIR, exist_ok=True)
        gdown.download(id=DECODER_ID, output=DECODER_PATH, quiet=False)
        print("decoder_final.pth downloaded!")
    else:
        print("decoder_final.pth already exists, skipping.")

if __name__ == "__main__":
    download()
