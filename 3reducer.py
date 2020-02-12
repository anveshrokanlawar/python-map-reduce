s = open("02.txt","r")
r = open("03.txt", "w")

counter = 0
thiskey = ""
thisvalue = 0


for line in s:
  data = line.strip().split('\t')
  paymentType, store = data

  if thiskey == "":
    if paymentType:
      thiskey = paymentType

  # apply the aggregation function
  
  if paymentType == thiskey:
    counter = counter + 1
  else:
    r.write( thiskey + '\t' + str(counter)+'\n')
    # start over when changing keys
    thiskey = paymentType
    counter = 1

  # output final entry
r.write( thiskey + '\t' + str(counter)+'\n')

s.close()
r.close()
