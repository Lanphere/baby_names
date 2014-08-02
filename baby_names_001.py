
import re

def main():

  '''
  this script attempts to follow the lesson for google python "baby names" sorting by alphabetical
  order, and writing out a list of boy/girl names with corresponding popularity ranking
  '''

  f = open('baby1990.html', 'r')
  writeFile = open('writeTestNames.txt','w')

  myDict = {}

  # year match
  for lineDate in f.readlines():
    strYear = ''.join(lineDate)
    matchYear = re.search(r'h3.*(\d\d\d\d)', strYear)

    if matchYear:
      writeFile.write(matchYear.group(1)+'\n\n')

  # names match
  g = open('baby1990.html', 'r')
  for lineNames in g.readlines():
    strNames = ''.join(lineNames)
    matchStr = re.search(r'<td>(\d*)</td><td>(\w*)</td><td>(\w*)</td>', strNames)

    # group 1 is rank, 2 is boy's name, 3 is girl's name
    if matchStr and not matchStr.group(2) in myDict:
      myDict[matchStr.group(2)] = matchStr.group(1)

    if matchStr and not matchStr.group(3) in myDict:
      myDict[matchStr.group(3)] = matchStr.group(1)

  for key in sorted(myDict):
    writeFile.write(key +  '   ' + myDict[key] + '\n')

  writeFile.close()
  f.close()
  g.close()


















if __name__=='__main__':
  main()
