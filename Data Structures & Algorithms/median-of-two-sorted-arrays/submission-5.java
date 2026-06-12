class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int m= nums1.length;
        int n=nums2.length;
        int x= m+n;
        int[] num=new int[x];
        for(int i=0;i<m;i++){
            num[i]=nums1[i];
        }
        for(int i=0;i<n;i++){
            num[m+i]=nums2[i];
        }
        Arrays.sort(num);
        if(x%2==0){
            int n1=(x/2)-1;
            int n2=(x/2);
            double ans=(num[n1]+num[n2])/2.0;
            return ans;
        }
        else{
            int k2=(x/2);
            int ans=num[k2];
            return ans;
        }
    }
}
