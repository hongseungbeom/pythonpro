def frequency_analytic(s):
  counts = {}
  for alpb in s:
    ltr = alpb
    if ltr not in counts:
      counts[ltr] = 0
    counts[ltr] += 1 
  for ltr in sorted(counts.keys()):
    print(ltr, counts[ltr])

if __name__ =="__main__":
  msg = input('input your message :')
  frequency_analytic(msg)
