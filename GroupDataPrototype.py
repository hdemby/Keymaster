
path = input("Path? ")

def minspace(lline):
  "remove extra space in lline data text"
  #print(lline.split(' '))
  while lline.find('\t') > -1:
    lline = lline.replace('\t',' ')
  while lline.find('  ') > -1:
    lline = lline.replace('  ',' ')
    #print(lline.split(' '))
  return lline.rstrip()

def GroupData(data):
  "organize data by group"
  grp = 'Group1'
  for each in data:
    if each.find('Group') > -1:
      idx = each.find('Group')    
      grp = each[idx:idx + 6]
    elif each.find('-----') > -1:
      return
    elif each[0]==' ':
      eachlst = minspace(each).split(' ')
      eachlst[0] = grp
      print(eachlst)
  return
  
def runTheCode():
  "run the code"
  keyfile = True and input("Which file?") or 'clues20220131.txt'
  data = open(f"{path}{keyfile}",'rt').readlines()
  GroupData(data)

if __name__ == '__main__':
  "run the code"
  runTheCode()
