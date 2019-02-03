import unittest
import random
def partition(arr, start, end):
    pivot = arr[start]
    leftmark = start + 1
    rightmark = end
    done = False
    while not done:
        # Find left mark
        while leftmark <= rightmark and arr[leftmark] <= pivot:
            leftmark += 1
        # Find right mark
        while rightmark >= leftmark and arr[rightmark] >= pivot:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            # Swap items
            arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]


    # Swap pivot and right mark
    arr[start], arr[rightmark] = arr[rightmark], arr[start]
    return rightmark

def quicksort(arr, start, end):
    if start < end:
        # Find split point and move items each side of pivot
        split = partition(arr, start, end)
        # Sort left half
        quicksort(arr, start, split - 1)
        # Sort right half
        quicksort(arr, split + 1, end)
    return arr


class quicksortTest(unittest.TestCase):
    def testRandomList(self):
        arr = [2, 5, 2, 7, 2, 75, 34, 67]
        self.assertEqual(quicksort(arr, 0, len(arr)-1), [2, 2, 2, 5, 7, 34, 67, 75])

    def testOrderedList(self):
        arr = [2, 2, 2, 5, 7, 34, 67, 75]
        self.assertEqual(quicksort(arr, 0, len(arr)-1), [2, 2, 2, 5, 7, 34, 67, 75])

    def testReversedList(self):
        arr = [75, 67, 34, 7, 5, 2, 2, 2]
        self.assertEqual(quicksort(arr, 0, len(arr)-1), [2, 2, 2, 5, 7, 34, 67, 75])

if __name__ == '__main__':
    unittest.main()

