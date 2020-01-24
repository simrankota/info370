# error handling
# f = {}
# for w in sentence.lower().split():
#     try:
#         f[w] += 1
#     except:
#         f[w] = 1

# { w:sentence.count(w) for w in sentence.lower().split()}
words = ['mps-803x', 'info201a', 'gg33--44.a5']
import re
w1 = [re.sub('[0-9]', '', x) for x in words]
[ re.search('[0-9]', x) for x in w1]