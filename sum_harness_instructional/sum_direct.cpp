#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>



void 
setup(int64_t N, uint64_t A[])
{

   printf(" inside direct_sum problem_setup, N=%lld \n", N);
      for (int64_t i = 0; i < N; i++) {
        A[i] = i + 1;
    }
}

int64_t
sum(int64_t N, uint64_t A[])
{
   int sum = 0;
   
for (int i=0; i<= size_t(A); i++){
   int64_t sum = 0;
   sum = N + A[i];
   }
   printf(" inside direct_sum perform_sum, N=%lld \n", N);
   
   return sum;
}

