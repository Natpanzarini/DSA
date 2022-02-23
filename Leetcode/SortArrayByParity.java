class Solution {
    public int[] sortArrayByParityII(int[] A) {
        //Two Pointer:
            //Left pointer: checks if mod of element matches mod of index
               //if not:
                    //right pointer: find the opposite case found by left (even elem at odd                         index if left found odd elem at even index), and swaps.
                    //increment left
                //if yes: move on

            //stop when left has gone through the array once

        //Runtime: O(n + n/2) - 9ms,7.94%
        //Space: O(1) - 96.30%

        for(int j = 0; j < A.length; j++){
            if(j % 2 == 0 && A[j] % 2 == 1){ //index even, element odd
                for(int i = j + 1; i < A.length; i++){
                    if(i % 2 == 1 && A[i] % 2 == 0){//index odd, element even
                        //swap
                        int temp = A[j];
                        A[j] = A[i];
                        A[i] = temp;
                        break;
                    }
                }
            }


            if(j % 2 == 1 && A[j] % 2 == 0){//index odd, element even
                for(int i = j + 1; i < A.length; i++){
                    if(i % 2 == 0 && A[i] % 2 == 1){//index even, element odd
                        //swap
                        int temp = A[j];
                        A[j] = A[i];
                        A[i] = temp;
                        break;
                    }
                }

            }

        }
        return A;

    }
}
