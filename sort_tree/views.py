from django.shortcuts import render
from django.http import HttpResponse
import json
import queue

def homepage(request):
    return render(request, 'home.html')

def select(request):
    data = request.GET['ds']
    if data == "tr":
        return render(request, 'tree.html')
    else:
        return render(request, 'sort.html')

def tree1(request):
    input=request.GET['tree_input']
    arr=input.split()
    class Node:
        def __init__(self, d):
            self.data = d
            self.left = None
            self.right = None

    def array_to_bst(arr):
        if not arr:
            return None
        mid = int((len(arr)) / 2)
        root = Node(arr[mid])
        root.left = array_to_bst(arr[:mid])
        root.right = array_to_bst(arr[mid + 1:])
        return root

    def preOrder(node):
        if not node:
            return

        ans.append(node.data)
        preOrder(node.left)
        preOrder(node.right)

    def printLevelOrder(root):

        if not root:
            return

        q = queue.Queue()

        q.put(root)

        while not q.empty():

            nodeCount = q.qsize()
            flag=0
            x=0

            while nodeCount > 0:
                flag=1
                node = q.queue[0]
                x=x+int(node.data)
                q.get()
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
                nodeCount = nodeCount - 1
            if flag==1:
                ans1.append(x)

    ans = list()
    ans1=list()
    arr.sort(key=int)
    root = array_to_bst(arr)
    preOrder(root)
    printLevelOrder(root)

    d=dict()
    d['preoder']=ans
    d['level_sum']=ans1
    return HttpResponse(json.dumps( d))

def sort(request):
    input1 = request.GET['sort_input']
    arr1 = input1.split()
    n=len(arr1)
    def partition(arr1, low, high):
        i = low - 1
        pivot = arr1[high]
        for j in range(low, high):
            if arr1[j] <= pivot:
                i = i + 1
                arr1[j], arr1[i] = arr1[i], arr1[j]
        arr1[i + 1], arr1[high] = arr1[high], arr1[i + 1]
        return i + 1

    def quick_sort(arr1, low, high):
        if low < high:
            pi = partition(arr1, low, high)
            quick_sort(arr1, low, pi - 1)
            quick_sort(arr1, pi + 1, high)


    quick_sort(arr1, 0, n - 1)
    out1 = json.dumps(arr1)
    return HttpResponse(out1)