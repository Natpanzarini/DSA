class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # Brute force:
            # find time from one point in the list to the next.
            # store each time in a list
            # sum the list when you run out of points
            # return sum

        # Runtime: O(n)
        # Space: O(n-1 + 4) -> list of distances (n - 1) + 4 pointers

        # Runtime: 64ms, 42.32%
        # Memory: 13.9mb, 100%

        time_between_points = []

        for index, point in enumerate(points):
            x,y = points[index]
            if index < len(points) - 1:
                i,j = points[index + 1]
                # the difference is the largest difference between (x1 - x) or (y1 - y)
                dist = max(abs(i - x),abs(j - y))
                time_between_points.append(dist)

        return sum(time_between_points)
