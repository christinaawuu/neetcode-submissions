class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int sum = 0;
        int left = 0;
        int right = numbers.size() - 1;

        for(int i = 0; i < numbers.size(); i++) {
            sum = numbers[left] + numbers[right];

            if(sum < target) {
                left += 1;
            } else if (sum > target) {
                right -= 1;
            } else if (sum == target) {
                return {left + 1, right + 1}; // using 1 indexed arr
            }
        }
        return {};
    }
};
