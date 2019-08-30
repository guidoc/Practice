
import random
import numpy as np





def kmeans(listOfPoints, k):
    print 'boo'
    # init k random centroids


    # assign each point to the closest centroid



    # update centroids of each cluster until convergence


def dist(points, centroid):
    return [np.linalg.norm(point - centroid, 2) for point in points]


if __name__ == "__main__":
    # generate 500 random 2d points
    numPoints = 500
    ptMin = 0
    ptMax = 100
    points = np.array([np.array([random.randint(ptMin,ptMax), random.randint(ptMin,ptMax)]) for i in range(numPoints)])

    # generate k random centroids
    numCentroids = 5
    centroids = np.array([np.array([random.randint(ptMin,ptMax), random.randint(ptMin,ptMax)]) for i in range(numCentroids)])

    while True:
        clusters = []*len(centroid)
        for point in points:
            for centroid in centroids:
                dist =


        # compute distance
        dist = [dist(points, centroid) for centroid in centroids]


    print 'boo'