class Solution {
  public:
    long long int count(int coins[], int N, int sum) {

        long long int table[sum + 1];
        memset(table, 0, sizeof(table));
        table[0] = 1;
        for (int i = 0; i < N; i++)
            for (int j = coins[i]; j <= sum; j++) table[j] += table[j - coins[i]];

        return table[sum];
    }
};
