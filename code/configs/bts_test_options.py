from configs.test_options import TestOptions

class BtsTestOptions(TestOptions):
    def initialize(self):
        parser = TestOptions.initialize(self)  

        parser.add_argument('--encoder',                   type=str,   help='type of encoder, desenet121_bts, densenet161_bts, '
                                                            'resnet101_bts, resnet50_bts, resnext50_bts or resnext101_bts',
                                                        default='densenet161_bts')
        # Training
        parser.add_argument('--fix_first_conv_blocks',                 help='if set, will fix the first two conv blocks', action='store_true')
        parser.add_argument('--fix_first_conv_block',                  help='if set, will fix the first conv block', action='store_true')
        parser.add_argument('--bn_no_track_stats',                     help='if set, will not track running stats in batch norm layers', action='store_true')
        parser.add_argument('--weight_decay',              type=float, help='weight decay factor for optimization', default=1e-2)
        parser.add_argument('--bts_size',                  type=int,   help='initial num_filters in bts', default=512)
        parser.add_argument('--retrain',                               help='if used with checkpoint_path, will restart training from step zero', action='store_true')
        parser.add_argument('--adam_eps',                  type=float, help='epsilon in Adam optimizer', default=1e-6)
        parser.add_argument('--learning_rate',             type=float, help='initial learning rate', default=1e-4)
        parser.add_argument('--end_learning_rate',         type=float, help='end learning rate', default=-1)
        parser.add_argument('--variance_focus',            type=float, help='lambda in paper: [0, 1], higher value more focus on minimizing variance of error', default=0.85)


        return parser


