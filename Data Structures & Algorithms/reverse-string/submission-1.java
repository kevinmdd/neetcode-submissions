class Solution 
{
    public void reverseString(char[] s) 
    {
        int end = 0;
        int start = s.length-1;
        while (start > end)
        {
            char temp = s[start];
            s[start] = s[end];
            s[end] = temp;
            end++;
            start--;
        }
    }
}