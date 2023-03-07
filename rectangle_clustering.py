from sklearn.cluster import DBSCAN
import numpy as np

def task4(rectangles):
    '''Finds the center of each rectangle and uses it to find clusters. For each cluster, it returns the mean position, width and height.'''

    # Calculate the center coordinates of each rectangle
    centers = rectangles[:, :2] + 0.5 * rectangles[:, 2:]

    # Perform DBSCAN clustering based on the center coordinates
    dbscan = DBSCAN(eps=15, min_samples=2)
    clusters = dbscan.fit_predict(centers)

    # Print the clusters and their corresponding rectangles
    mean_recs = []
    for cluster in np.unique(clusters):
        print(f"Cluster {cluster}:")
        recs = rectangles[clusters == cluster]
        for rect in rectangles[clusters == cluster]:
            print(f"  ({rect[0]}, {rect[1]}) w={rect[2]}, h={rect[3]}")
        x = np.mean(recs[:,0])
        y = np.mean(recs[:,1])
        w = np.mean(recs[:,2])
        h = np.mean(recs[:,3])
        mean_recs = np.append(mean_recs, np.array([[x,y,w,h]]), axis=0)
        print(f"  Mean Values:")
        print(f"  ({x}, {y}, w={w}, h={h}")
        
    return(mean_recs)
