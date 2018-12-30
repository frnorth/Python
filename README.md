# mypython

split\_merge\_sort.py 中
分割的时候，(left, middle) (middle+1, right)
不要(left, middle-1)  (middle, right)
合并的时候，第一个判断要：if left>middle 不要 left>middle-1 (left>=middle?)
不然的话，最底层两个数字分不开
