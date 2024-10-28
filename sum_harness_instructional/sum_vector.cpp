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
    int64_t i;
    for (i = 0; i <= N - 4; i += 4) {
        total += A[i] + A[i + 1] + A[i + 2] + A[i + 3];
    }
    for (; i < N; ++i) {
        total += A[i];
    }
   printf(" inside sum_vector perform_sum, N=%ld \n", N);
   return total;
}

