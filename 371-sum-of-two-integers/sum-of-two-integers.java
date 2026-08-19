class Solution {
    public int getSum(int a, int b) {
        while (b != 0){
            int temp = (a & b) << 1;        // a AND b (1,1) = 1 else 0 and <<1(shifted left by 1)
            a = a ^ b;      // a XOR b  (1,1),(0,0) = 0, (1,0),(0,1) = 1
            b = temp;    
        }
        return a;
    }
}