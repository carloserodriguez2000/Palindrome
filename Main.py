################################################################################
# hi. This program plays a game inspired by the TV show "BigBang Theory".
def cleanS ( string ):
    cleanS = string.strip()              # get read off Leading and training spaces.
    cleanS = cleanS.lower()
    return cleanS
        


def main ():

    sLine = input( 'Enter a word or phrase to check palindrome: ')
    sLine = cleanS( sLine)
    indexer = list()
    sLen = len(sLine)
    indexer = range(sLen)     #Create an array for 0:len(
    sReverse = list()
    sReverseLine = ''
    
    for index in indexer :
        ##print ((sLen-1)-index)
        sReverse.append( sLine[(sLen-1)-index])
        sReverseLine +=  sReverse[index]
        ##print(index)

    print(sLine)
    print(sReverse)
    print(sReverseLine)
    if( sLine == sReverseLine):
        print( 'String \"%s\" is a palindrome' %(sLine))

################################################################################
#
################################################################################
main()
