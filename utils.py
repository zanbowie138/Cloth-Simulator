import math;
def get_distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def pixel(surface, color, pos):
    surface.fill(color, (pos, (1, 1)))

def get_length(arr):
    return math.sqrt(arr[0]**2 + arr[1]**2)

def normalize(arr):
    length = get_length(arr)
    return [arr[0]/length,arr[1]/length]

def get_unit_vec(arr1, arr2):
    change = sub(arr1, arr2)
    if (get_length(change)) == 0:
        return [0.0,0.0]
    return normalize(change)

def add(*arrs):
    output = [0,0]
    for arr in arrs:
        output[0] += arr[0]
        output[1] += arr[1]
    return output

def sub(arr1, arr2):
    output = [0,0]
    output[0] = arr1[0] - arr2[0]
    output[1] = arr1[1] - arr2[1]
    return output

def mult_scalar(arr, scalar):
    return [arr[0]*scalar, arr[1]*scalar]