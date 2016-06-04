import os, shutil, math
path="C:\\Users\\Jay\\Desktop\\split cards\\images\\sorted"  # insert the path to the directory of interest
sorted_path="C:\\Users\\Jay\\Desktop\\split cards\\images\\sorted2"
list_of_files = []
temp_list =[]
dirList=os.listdir(path)
for fname in dirList:
    list_of_files.append(fname)
    
card_number = 1
old_list_of_cards = []
new_list_of_cards = []
list_of_cards = []
link = []

for I in range(0,12):
    list_of_cards.append([])


for word in list_of_files:
    full_path = path + "\\" + word
    tempnum = word[:2]
    print "tempnum:" + tempnum
    if int(tempnum) %12 !=0:
        list_of_cards[int(tempnum)%12-1].append(tempnum)
    else:
        list_of_cards[11].append(tempnum)
    #if tempnum >= "03" and tempnum != "15" and tempnum != "52":
        
        #if tempnum < 15:
            #new_list_of_cards.append(int(tempnum) -2)
        #else:
            #new_list_of_cards.append(int(tempnum) -3)
        #modo = int(card_number) % 12
        #divo = math.ceil(int(card_number) / 12.0)
        #if modo == 0:
            #modo = 12
        #print "%12:" + str(modo)
        #print "/12:" + str(divo)    
        ##if modo == 0:
        ##    file_name = str(int((card_number%12 + divo + 1)* divo))
        ##else:
        #file_name = str(int(modo * divo))
        #if int(tempnum) <15:
            #file_name = int(tempnum ) - 2
        #else:
            #file_name = int(tempnum ) - 3
        ##if file_name == "0":
        ##    file_name = "45"        
        #print file_name
        #card_number+= 1
        #full_dest_name = sorted_path + "\\" + str(file_name) + ".jpg"
        #print full_dest_name
        #shutil.copyfile(full_path, full_dest_name)
print list_of_cards
month = 1
cardNum = 1
for listx in list_of_cards:
    for card in listx:
        fileName = cardNum
        cardNum+=1
        print card
        print fileName
        #file names [card-1] + blah full path 
        sourcePath = path + "//" +list_of_files[int(card)-1]
        full_dest_path = sorted_path + "\\" + str(fileName) + ".jpg"
        print full_dest_path
        shutil.copyfile(sourcePath, full_dest_path)
        
#print list_of_files
#for card_num in new_list_of_cards:
#    print card_num