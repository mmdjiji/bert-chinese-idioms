#coding=utf-8
from transformers import BertTokenizer, BertForMaskedLM
import torch
import numpy as np

bert_path = 'mmdjiji/bert-chinese-idioms' # 'model/bert'
tokenizer = BertTokenizer.from_pretrained(bert_path)
model = BertForMaskedLM.from_pretrained(bert_path)
    
def bert_ppl(sent, model, tokenizer):
  model.eval()
  
  tokenize_input = tokenizer.tokenize(sent)
  tensor_input = torch.tensor([tokenizer.convert_tokens_to_ids(tokenize_input)])

  sen_len = len(tokenize_input)

  sent_loss = 0.

  for i, word in enumerate(tokenize_input):
    tokenize_input[i] = tokenizer.mask_token
    mask_input = torch.tensor([tokenizer.convert_tokens_to_ids(tokenize_input)])
    output = model(mask_input)
    pred_scores = output[0]
    ps = torch.log_softmax(pred_scores[0, i], dim=0)
    word_loss = ps[tensor_input[0, i]]
    sent_loss += word_loss.item()
    tokenize_input[i] = word   # restore
  print("sent loss", sent_loss)
  ppl = np.exp(-sent_loss/sen_len)

  return ppl

def ppl(sentence):
  return bert_ppl(sentence, model, tokenizer)

if __name__ == '__main__':
  sentences = ['今天的天气万里无云', '今天的天气疏而不漏', '今天的天气束手就擒']
  for sentence in sentences:
    print(bert_ppl(sentence, model, tokenizer))