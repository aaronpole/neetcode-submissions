class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char,int> dict1, dict2;
        for (char c : s){
            dict1[c]++;
        }
        for (char c : t){
            dict2[c]++;
        }
        return dict1 == dict2;
    }
};
