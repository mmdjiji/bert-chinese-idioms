from django.http import HttpResponse

from . import bert

def controller_bert(request): # ?ctx=今天的天气[MASK]&candidates=风和日丽,恐怖如斯,语言模型
  request.encoding='utf-8'
  if 'ctx' in request.GET and 'candidates' in request.GET:
    candidates = request.GET['candidates'].split(',')
    ctx = request.GET['ctx']
    score = 0x3f3f3f3f
    best = ''
    for i in candidates:
      trial = ctx.replace('[MASK]', i)
      trial_score = bert.ppl(trial)
      if trial_score < score:
        score = trial_score
        best = trial

  response = best
  
  return HttpResponse(response)