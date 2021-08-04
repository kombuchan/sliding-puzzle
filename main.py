from puzzle import *
if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser(description="Sliding puzzle")
    parser.add_option('-i', '--image', type=str, default='img.png',
                      help="path to image")
    args, _ = parser.parse_args()

    app = Puzzle(args.image, 3)
    app.master.title('Sliding puzzle')
    app.mainloop()