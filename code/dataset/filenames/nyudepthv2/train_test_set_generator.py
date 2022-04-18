#creates a txt file of training images, a subset of all available training images
#selected images are evenly distributed from total samples
import os
import sys

def main():
    if len(sys.argv)<3:
        print("Enter two numbers, one for train subset size, one for test subset size")
        return
    train_subset_size = min(int(sys.argv[1]),24231)
    test_subset_size = min(int(sys.argv[2]),654)
    script_dir = os.path.join(os.path.dirname(__file__),str(train_subset_size)+"_"+str(test_subset_size))
    os.makedirs(script_dir, exist_ok=True)


    train_file_name = 'train_subset.txt'
    test_file_name = 'test_subset.txt'

    train = open(os.path.join(script_dir,train_file_name), 'w')
    test = open(os.path.join(script_dir,test_file_name), 'w')
    with open(os.path.join(os.path.dirname(__file__),'train_list.txt'), 'r') as r:
        sorted_r = sorted(r)
        for i in range(train_subset_size):
            line=sorted_r[round(i*24231/train_subset_size)]
            train.write(line)
    train.close()
    with open(os.path.join(os.path.dirname(__file__),'test_list.txt'), 'r') as r:
        sorted_r = sorted(r)
        for i in range(test_subset_size):
            line=sorted_r[round(i*654/test_subset_size)]
            test.write(line)
    test.close()
    return


if __name__ == '__main__':
    main()