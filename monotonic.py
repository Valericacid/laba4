def is_monotonic(nums):
    increasing = sorted(nums)
    waning  = sorted(nums, reverse = True)
    if nums == waning or nums == increasing :
        return True
    else:
        return False


