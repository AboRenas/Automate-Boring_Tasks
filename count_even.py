# def even_numbers(n):
#     count = 0
#     current_number = 0
#     while current_number < n:
#         if current_number % 2 == 0:
#             count += 1
#             current_number += 1
#
#
# def divisble(max, divisor):
#     count = 0

#     for x in range(1, max + 1):
#         if x % divisor == 0:
#             count += 1
#         return count

def count_numbers(first, last):
  # Loop through the numbers from first to last
  x = first #2
  while x <= last:
      print(x)
      x = x +1

count_numbers(2,6)
