class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> dup;

        for (int i : nums) {
            if(dup.contains(i)) {
                return true;
            } else {
                dup.insert(i);
            }
        }
        return false;
    }
};