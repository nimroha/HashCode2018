
import sys
import argparse

from src.Parser import parseIn, parseOut
from src.Graph import Graph

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
    # build graph
    graph = Graph(rows, cols, maxTime)

    #TODO add weights

    schedule = []
    for i in numCars:
        edges = graph.find_shortest_path()
        ridesTaken = []
        for edge in edges:
            if 'label' in edge:
                ridesTaken.append(edge['label'])
        ridesTaken.sort()
        schedule.append(ridesTaken)
        graph.remove_rides(ridesTaken)

    print("Writing solution to file...")
    parseOut(outPath, schedule)

    print("Done")


if __name__ == '__main__' :
    sys.exit(main())
