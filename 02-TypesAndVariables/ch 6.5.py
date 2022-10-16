line = 'X-DSPAM-Confidence:0.8475'
slice = float(line[line.find(':')+1:])
print(slice)