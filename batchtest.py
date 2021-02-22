
import numpy as np
import torch

from hparams import Create

from train import load_model
from text import text_to_sequence
from text.process_text import generateSegemnts, generateSegemnts_from_file

def generate_from_file(file_name,wavglow_path,checkpoint_path):
    with open(file_name, "rb") as text:
        sentences=generateSegemnts_from_file(file_name)
        audio=batch_inference(sentences,wavglow_path,checkpoint_path)
    return audio


def batch_inference(sentences,waveglow_path,checkpoint_path):


     hparams = Create()
     hparams.sampling_rate = 22050
     print("loading tacotron model")
     model = load_model(hparams)

     model.load_state_dict(torch.load(checkpoint_path)['state_dict'])
     _ = model.cuda().eval().half()
     from waveglow.denoiser import Denoiser
     print("loading waveglow model")
     waveglow = torch.load(waveglow_path)['model']
     waveglow.cuda().eval().half()
     for k in waveglow.convinv:
         k.float()
     denoiser = Denoiser(waveglow)
     print("processing text")
     import wave
     au = np.array([])

     for line in sentences:
             sequence = np.array(text_to_sequence(line, ['english_cleaners']))[None, :]
             sequence = torch.autograd.Variable(
                 torch.from_numpy(sequence)).cuda().long()

             mel_outputs, mel_outputs_postnet, _, alignments = model.inference(sequence)

             with torch.no_grad():
                 audio = waveglow.infer(mel_outputs_postnet, sigma=0.666)
                 audio_denoised = denoiser(audio, strength=0.01)[:, 0]
                 au = np.concatenate((au, audio_denoised.cpu().numpy()), axis=None)
     return au







if __name__ == '__main__':
    filen="/home/eden/test.txt"
    generate_from_file(filen)
