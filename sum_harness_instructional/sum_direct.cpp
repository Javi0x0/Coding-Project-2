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
      for (int64_t i = 0; i < N; i++) {
        A[i] = i + 1;
    }
   printf(" inside direct_sum problem_setup, N=%ld \n", N);
}

int64_t
sum(int64_t N, uint64_t A[])
{ 
    int64_t sum = 0;
for (int i=0; i < N; i++){
   sum += A[i];
   }
   printf(" inside direct_sum perform_sum, N=%ld \n", N);
   
   return sum;
}

