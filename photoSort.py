import os

def movePhotoToFront(dirName):
    print "processing " + dirName
    dirStack = []
    for sub_dir in os.listdir(dirName):
        dirStack.append(sub_dir)
    while len(dirStack) != 0 :
        top = dirStack[-1]
        dirStack.pop()
        if( os.path.isdir( dirName + "/" + top) ):
            for sub_dir in os.listdir(dirName + "/" + top):
                dirStack.append(top + '/' + sub_dir)
        else:
            old_path = dirName + "/" + top
            new_path = dirName + "/" + top.split('/')[-1]
            print "moving " + old_path + " to " + new_path
            os.rename(old_path, new_path)

    print "end processing " + dirName

def main():
    d1 = "/home/user/Desktop/Photos/2016"
    d2 = "/home/user/Desktop/Photos/2017"
    d3 = "/home/user/Desktop/Photos/2018"
    d4 = "/home/user/Desktop/Photos/2019"
    movePhotoToFront(d1)
    movePhotoToFront(d2)
    movePhotoToFront(d3)
    movePhotoToFront(d4)

    

if __name__ == "__main__":
    main()