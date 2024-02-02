def merge(nums1, nums2):
    i = len(nums1) - len(nums2) - 1
    j = len(nums2) - 1
    k = len(nums1) - 1 

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    for num in nums1:
        print(num)

merge([4,5,6,0,0,0],[1,2,3])
