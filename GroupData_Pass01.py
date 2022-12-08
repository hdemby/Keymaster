"""
Code to manage, organize and group 'clues*' key files
"""
PATH = r"C:/Users/hdemb/Dropbox/Documents/Family/keys/"
DEBUG = 0

def minspace(lline):
  "remove extra space in lline data text"
  #print(lline.split(' '))
  while lline.find('\t') > -1:
    lline = lline.replace('\t',' ')
  while lline.find('  ') > -1:
    lline = lline.replace('  ',' ')
    if DEBUG > 1:
      print(lline.split(' '))
  return lline.rstrip()

def GroupData(data):
  "organize data by group"
  groupdata = []
  grp = 'Group1'
  for each in data:
    each = each.replace(':','')
    if each.find('Group') > -1:
      #set the group ID:
      idx = each.find('Group')    
      grp = each[idx:idx + 6]
    elif each.find('-----') > -1:
      #stop at end of keys section of file:
      break
    elif each[0] == " ":
      #extract data fields from input:
      each[0]==' '
      eachlst = minspace(each).split(' ')
      eachlst[0] = grp
      groupdata.append(eachlst)
      if DEBUG:
        print(len(groupdata),eachlst)
    else:
      pass
  return groupdata
  
def getPWDs(datalst):
  "return set of existing passwords"
  pwset = set()
  for each in datalst:
    try:
      pwset.add(each[3])
    except:
      print("skipped: {each}")
  return pwset
  
def ShowList(datalst):
  "display the data"
  for each in datalst:
    try:
      print(f"{len(each)}\t{each[1]}\t{each[2]}\t{each[3]}\t\t{each}")
    except:
      pass
  return

def ColumPrint(listinfo, cols = 6):
  "print information in defined number of columns"
  reset = 0
  itms = listinfo
  last = len(itms) % cols
  curcol = 0
  for itm in itms:
    try:
      if curcol < cols:
        print(itm, end=", ")
        curcol +=1
      else:
        print()
        curcol = 0
    except:
      print(f"{itm}, " for itm in itms[last:])
  return

def getPassLst(data):
  "return the unique pwd clues found"
  clues = set()
  for each in data:
    try:
      clues.add(each)
    except:
      print(f"Skipped: {each}")
  return clues
  
def runTheCode(path=PATH):
  "run the code"
  keyfile = True and input("Which file?") or 'clues20220131.txt'
  data = open(f"{path}{keyfile}",'rt').readlines()
  keylst = GroupData(data)
  return keylst


if __name__ == '__main__':
  "run the code"
  data = runTheCode()
  print(f"There are {len(data)} items in this report")
  ShowList(data)
  clues = getPWDs(data)
  print(clues)
  uniq = getPassLst(clues)
  print(f"There are {len(uniq)} clues in this list")
  print(f"\nThe uniq clues are:")
  ColumPrint(sorted(uniq),1)
  