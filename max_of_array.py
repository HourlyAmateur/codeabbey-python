str_list = input().split()
int_list = [int(x) for x in str_list]
print(max(int_list), end=' ')
print(min(int_list))