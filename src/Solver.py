
import sys
import argparse

from src.Parser import parseIn, parseOut

def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(description='Solve car sharing problem')

    parser.add_argument('--input_file',   help='Path to input file.', required=True)
    parser.add_argument('--output_file',  help='Path to output file', required=True)

    args = parser.parse_args()
    inPath  = args.input_file
    outPath = args.output_file

    print("Parsing...")
    rides, rows, cols, numCars, numRides, bonus, maxTime = parseIn(inPath)
    print("numCars: {n}, numRides: {m}, gridSize: ({y}x{x}), totalTime: {t}".format(n=numCars,
                                                                                    m=numRides,
                                                                                    x=cols,
                                                                                    y=rows,
                                                                                    t=maxTime))

    print("Solving...")
    #TODO solve problem

    print("Writing solution to file...")
    schedule = []
    parseOut(outPath, schedule)

    print("Done")


if __name__ == '__main__' :
    sys.exit(main())
