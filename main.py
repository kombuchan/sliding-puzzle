from puzzle import *
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser(description="Sliding puzzle")
    parser.add_option('-g', '--board-grid', type=int, default=3,
                      help=" Board must be 3x3 or larger! ")
    parser.add_option('-i', '--image', type=str, default='img2.png',
                      help="path to image")
    args, _ = parser.parse_args()

    if args.board_grid < 3:
        args.board_grid = 3
        print ("The board size you have chosen is too small... Setting board size to 3...")

    app = Puzzle(args.image, args.board_grid)
    app.master.title('Sliding puzzle')
    app.mainloop()