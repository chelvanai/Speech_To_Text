from transformers import AutoTokenizer, Wav2Vec2ForCTC


tokenizer = AutoTokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")


# speech, rate = sf.read('LJ001-0002.wav')
# speech = librosa.resample(speech, rate, 160000)
#
#
# sp = torch.from_numpy(speech)
#
#
# input_values = tokenizer(sp, return_tensor='pt').input_values
#
#
# input_values = torch.from_numpy(input_values)
#
# # Store logits (non-normalized predictions)
# logits = model(input_values).logits
#
# # Store predicted id's
# predicted_ids = torch.argmax(logits, dim=-1)
#
# # decode the audio to generate text
# transcriptions = tokenizer.decode(predicted_ids[0])
# print(transcriptions)