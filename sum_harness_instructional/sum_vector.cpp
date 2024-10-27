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
   for (int64_t i = 0; i < N; ++i) {
       A[i] = i;
   }
   printf(" inside sum_vector problem_setup, N=%ld \n", N);
}

int64_t
sum(int64_t N, uint64_t A[])
{
   int64_t total = 0;
   for (int64_t i = 0; i < N; ++i) {
       total += A[i];
   }
   printf(" inside sum_vector perform_sum, N=%ld \n", N);

   return total;
}

