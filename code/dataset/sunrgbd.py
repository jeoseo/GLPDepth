import os
import cv2

from dataset.base_dataset import BaseDataset


class sunrgbd(BaseDataset):
    def __init__(self, data_path, filenames_path='./code/dataset/filenames/',
                 is_train=True, do_cutdepth=False, crop_size=(448, 576), scale_size=None):
        super().__init__(crop_size)

        self.scale_size = scale_size

        self.is_train = is_train

        self.image_path_list = []
        self.depth_path_list = []

        self.data_path=data_path
        self.do_cutdepth=do_cutdepth
        if is_train:
            filenames_path += '/train_subset.txt'
        else:
            filenames_path += '/test_subset.txt'


        self.filenames_list = self.readTXT(filenames_path)
        phase = 'train' if is_train else 'test'
        print("Dataset: SUNRGBD")
        print("# of %s images: %d" % (phase, len(self.filenames_list)))

    def __len__(self):
        return len(self.filenames_list)

    def __getitem__(self, idx):
        img_path = self.data_path + self.filenames_list[idx].split(' ')[0]
        gt_path = self.data_path + self.filenames_list[idx].split(' ')[1]
        filename = img_path.split('/')[-1]

        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        depth = cv2.imread(gt_path, cv2.IMREAD_UNCHANGED).astype('float32')

        #done because original image dimensions not divisible by 32
        H, W, C = image.shape
        image = cv2.resize(image, (W-(W %32), H-(H%32)))
        depth = cv2.resize(depth, (W-(W %32), H-(H%32)))
        if self.scale_size:
            image = cv2.resize(image, (self.scale_size[1], self.scale_size[0]))
            depth = cv2.resize(depth, (self.scale_size[1], self.scale_size[0]))
        if self.is_train and self.do_cutdepth:
            image, depth = self.augment_training_data(image, depth)
        else:
            image, depth = self.augment_test_data(image, depth)

        depth = depth / 10000.0  # convert in meters

        return {'image': image, 'depth': depth, 'filename': filename}
