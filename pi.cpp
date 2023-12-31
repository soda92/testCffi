/* filename: pi.c*/
#include "pi.h"
#include <math.h>
#include <stdlib.h>

/* Returns a very crude approximation of Pi
   given a int: a number of iteration */
float EXPORT PASCAL pi_approx(int n)
{
    double i, x, y, sum = 0;

    for (i = 0; i < n; i++)
    {

        x = rand();
        y = rand();

        if (sqrt(x * x + y * y) < sqrt((double)RAND_MAX * RAND_MAX))
            sum++;
    }

    return 4 * (float)sum / (float)n;
}