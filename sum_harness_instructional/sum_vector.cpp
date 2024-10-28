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
    int64_t sum = 0;
    int64_t i;
    for (i = 0; i < N; i += 2) {
        sum += A[i];
    if(i + 1 < N) {
        sum += A[i+1];
        }
    }
   printf(" inside sum_vector perform_sum, N=%ld \n", N);
   return sum;
}

