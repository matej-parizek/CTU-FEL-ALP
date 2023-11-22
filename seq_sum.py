nums = list(map(int, input().split()))
#počet slov
len_nums = len(nums)
nums.append(max(nums)+1)
# promenne
curr_sum = 0
curr_len = 0
prev_len = 0
prev_sum = 0
for i in range(0, len_nums):
    # podmínka stupňujícií se posloupnosti
    if nums[i+1] >= nums[i]:
        # podmínka pro čísla, která nejsou prvočísla
        if (nums [i] % 2 == 0) and (nums [i] / -2 != 1) and (nums [i] / 2 != 1):
            #podmínka pro nulování misí být u každé ho neprvočísla
            if (prev_len < curr_len) or (prev_len == curr_len) and (prev_sum < curr_sum):
                prev_len = curr_len
                prev_sum = curr_sum
            curr_len = 0
            curr_sum =0
        elif ( nums [i]% 3 == 0) and (nums [i] / -3 != 1) and(nums [i] / 3 != 1) :
            if (prev_len < curr_len) or (prev_len == curr_len) and (prev_sum < curr_sum):
                prev_len = curr_len
                prev_sum = curr_sum
            curr_len = 0
            curr_sum =0
        elif(nums [i] % 5 == 0) and (nums [i] / -5 != 1) and (nums [i] / 5 != 1):
            if (prev_len < curr_len) or (prev_len == curr_len) and (prev_sum < curr_sum):
                prev_len = curr_len
                prev_sum = curr_sum
            curr_len =0
            curr_sum = 0
        elif(nums [i] % 7 == 0) and (nums [i] / -7 != 1) and (nums [i] / 7 != 1):
            if (prev_len < curr_len) or (prev_len == curr_len) and (prev_sum < curr_sum):
                prev_len = curr_len
                prev_sum = curr_sum
            curr_len =0
            curr_sum =0
        elif (nums[i] == 1) or (nums == 0) or (nums[i]==-1):
            # dodat ke vsemu
            if (prev_len < curr_len) or (prev_len == curr_len) and (prev_sum < curr_sum):
                prev_len = curr_len
                prev_sum = curr_sum
            curr_len = 0
            curr_sum = 0
        # prvočísla
        else:
            if curr_len == 0:
                curr_len += 1
                curr_sum += nums[i]
            else:
                curr_sum += nums[i]
                curr_len += 1
    else:
        # podmínka pro čísla, která nejsou prvočísla
        if (nums [i] % 2 == 0) and (nums [i] / -2 != 1) and (nums [i] / 2 != 1):
            #podmínka pro nulování misí být u každé ho neprvočísla
            if (prev_len < curr_len) or (prev_len == curr_len) and (prev_sum < curr_sum):
                prev_len = curr_len
                prev_sum = curr_sum
            curr_len = 0
            curr_sum =0
        elif ( nums [i]% 3 == 0) and (nums [i] / -3 != 1) and(nums [i] / 3 != 1) :
            if (prev_len < curr_len) or (prev_len == curr_len) and (prev_sum < curr_sum):
                prev_len = curr_len
                prev_sum = curr_sum
            curr_len = 0
            curr_sum =0
        elif(nums [i] % 5 == 0) and (nums [i] / -5 != 1) and (nums [i] / 5 != 1):
            if (prev_len < curr_len) or (prev_len == curr_len) and (prev_sum < curr_sum):
                prev_len = curr_len
                prev_sum = curr_sum
            curr_len =0
            curr_sum = 0
        elif(nums [i] % 7 == 0) and (nums [i] / -7 != 1) and (nums [i] / 7 != 1):
            if (prev_len < curr_len) or (prev_len == curr_len) and (prev_sum < curr_sum):
                prev_len = curr_len
                prev_sum = curr_sum
            curr_len =0
            curr_sum =0
        elif (nums[i] == 1) or (nums == 0) or (nums[i]==-1):
            if (prev_len < curr_len) or (prev_len == curr_len) and (prev_sum < curr_sum):
                prev_len = curr_len
                prev_sum = curr_sum
            curr_len = 0
            curr_sum = 0
        else:
            if curr_len==0:
                curr_len+=1
                curr_sum += nums [i]
            else:
                curr_len += 1
                curr_sum += nums[i]
        if (prev_len < curr_len) or (prev_len == curr_len) and (prev_sum<curr_sum):
            prev_sum = curr_sum
            prev_len = curr_len
        curr_sum =0
        curr_len =0
# podmínka pro tisk, protože se curr_len a curr_vynulovává
if (prev_len < curr_len) or (prev_len == curr_len) and (prev_sum < curr_sum):
    print(curr_len)
    print(curr_sum)
else:
    print(prev_len)
    print(prev_sum)