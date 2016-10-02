import Ru_splitter

splitter = Ru_splitter.Splitter()

testfile = open("testtext.txt", 'r')
text = testfile.read()
testfile.close()

res = splitter.split(text)[:-1]
for i in res:
    print (i)