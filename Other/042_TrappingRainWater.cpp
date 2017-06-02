/*
Given n non-negative integers representing an elevation map where the width 
of each bar is 1, compute how much water it is able to trap after raining. 

For example, 
 Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6. 
*/

class Solution {
public:
    int trap(vector<int>& height) {
        
        int ml = 0;       // max from the left
        int mr = 0;       // max from the right
        int area = 0;
        int l = 0;                  // left pointer
        int r = height.size()-1;    // right pointer
      
        // two pointers
        while(l <= r)
        {
            ml = std::max(ml , height[l]);
            mr = std::max(mr , height[r]);
            
            // as long as *the other side* is higher, water will be trapped
            if(ml <= mr)
            {
                area+=ml-height[l++];
            }
            else
            {
                area+=mr-height[r--];
            }
        }
        return area;
    }
};
