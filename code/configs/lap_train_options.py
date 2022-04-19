from configs.train_options import TrainOptions

class LapTrainOptions(TrainOptions):
    def initialize(self):
        parser = TrainOptions.initialize(self)

        # Training and Testing setting
        parser.add_argument('--encoder', type=str, default = "ResNext101")
        parser.add_argument('--norm', type=str, default = "BN")
        parser.add_argument('--act', type=str, default = "ReLU")
        parser.add_argument('--img_save', action='store_true', help='result image save')
        parser.add_argument('--cap', default=80.0, type=float, metavar='MaxVal', help='cap setting for kitti eval')
        parser.add_argument('--height', type=int, default = 352)
        parser.add_argument('--width', type=int, default = 704)
        parser.add_argument('-e', '--evaluate', dest='evaluate', action='store_true', help='evaluate model on validation set')
        parser.add_argument('--lv6', action='store_true', help='use lv6 Laplacian decoder')

        parser.add_argument('--rank',                      type=int,   help='node rank for distributed training', default=0)
        return parser
