#creates a txt file of training images, a subset of all available training images
#selected images are evenly distributed from total samples
import os


#enter skip number for subset sizes (results will be approximate)
train_subset_size = 1000
#enter percentage of training set size to be the test set (eg 10 = 10%, max 100% obviously)
test_subset_percentage = 20
script_dir = os.path.join(os.path.dirname(__file__),str(train_subset_size))
os.makedirs(script_dir, exist_ok=True)

train_skip = train_subset_size/100
test_subset_size = int(train_subset_size*(test_subset_percentage*0.01))
test_skip = test_subset_size/100

train_file_name = 'train_subset.txt'
test_file_name = 'test_subset.txt'

train = open(os.path.join(script_dir,train_file_name), 'w')
test = open(os.path.join(script_dir,test_file_name), 'w')
with open(os.path.join(os.path.dirname(__file__),'train_list.txt'), 'r') as r:
    sorted_r = sorted(r)
    desired_train = sorted_r[0:len(sorted_r)-1:round(242.3/train_skip)]
    desired_test = sorted_r[1::round(242.3/test_skip)]
    for line in desired_train:
        train.write(line)
    for line in desired_test:
        test.write(line)
train.close()
