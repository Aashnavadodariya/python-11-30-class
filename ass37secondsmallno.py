nums = [1,2,3,4,4,3,3,0]
sm=float('inf')
ssm=float('inf')
for num in nums:
    if num <= sm:
        sm,ssm = num,sm
    elif num < ssm:
        ssm = num
        
        
        
