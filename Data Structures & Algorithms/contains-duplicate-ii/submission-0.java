class Solution 
{
    public boolean containsNearbyDuplicate(int[] nums, int k) 
    {
        boolean dupe = false;
        for (int i = 0; i < nums.length; i++)
        {
            for (int j = i+1; j < nums.length; j++)
            {
                if (nums[i] == nums[j])
                {
                    System.out.println(i);
                    System.out.println(j);
                    int absolute = Math.abs(i - j);
                    System.out.println(absolute);
                    if (absolute <= k)
                    {
                        dupe = true;
                        break;
                    }
                }
            }
        }
        return dupe;
    }
}