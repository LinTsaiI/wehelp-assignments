# 要求一:函式與流程控制
# 在函式中使用迴圈計算最小值到最大值之間，所有整數的總和。
def calculate(min, max):
  cal = 0
  for x in range(min, max+1):
    cal += x
  print(cal)

calculate(1, 3)
calculate(4, 8)



# 要求二:Python 字典與列表、JavaScript 物件與陣列
# 正確計算出員工的平均薪資，請考慮員工數量會變動的情況。
def avg(data):
  sum = 0
  for x in data['employees']:
    sum += x['salary']
  print(sum / data['count'])

avg({
  "count": 3,
  "employees": [
    {
      "name": "John",
      "salary": 30000
    },
    {
      "name": "Bob",
      "salary": 60000
    },
    {
      "name": "Jenny",
      "salary": 50000
    }
  ]
})  # 呼叫 avg 函式


# 要求三:演算法
# 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
# 不可以使用排序相關的內建函式。
def maxProduct(nums):
<<<<<<< HEAD
  n, numsNew = len(nums), []
  for i in range(n):
    for x in nums[(i+1):]:
      num = nums[i] * x
      numsNew.append(num)
  print(max(numsNew))

=======
  n = len(nums)
  numsNew = []
  for x in range(n):
    for y in nums[(x+1):]:
      num = nums[x] * y
      numsNew.append(num)
  print(max(numsNew))


>>>>>>> e89314e55044992ad95a3b54509d3716f7bab729
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2

<<<<<<< HEAD
# 另一個寫法
# def maxProduct(nums):
#   n = len(nums)
#   numsNew = []
#   for i in range(n):
#     for j in range(n):
#       if (i < j):
#         num = nums[i] * nums[j]
#         numsNew.append(num)
#   print(max(numsNew))

=======
>>>>>>> e89314e55044992ad95a3b54509d3716f7bab729


# 要求四 ( 請閱讀英文 ):演算法
# Given an array of integers, show indices of the two numbers such that they add up to a specific target. You can assume that each input would have exactly one solution, and you can not use the same element twice.
def twoSum(nums, target):
  n = len(nums)
  for x in range(n):
    for y in range(n):
      if (x != y) and (target == nums[x] + nums[y]):
        return [x, y]
  
result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9



# 要求五 (Optional): 演算法
# 給定只會包含 0 或 1 兩種數字的列表(Python) 或陣列(JavaScript)，計算連續出現 0 的最大長度。
def maxZeros(nums):
<<<<<<< HEAD
  counter, numsNew = 0, []
=======
  counter = 0
  numsNew = []
>>>>>>> e89314e55044992ad95a3b54509d3716f7bab729
  for x in nums:
    if x == 0:
      counter += 1
      numsNew.append(counter)
    else:
      numsNew.append(0)
      counter = 0
  print(max(numsNew))

maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3

