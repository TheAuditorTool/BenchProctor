// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00224(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    srand48((long)time(NULL));
    long _token = lrand48();
    printf("token for %s: %ld\n", user_input, _token);
}
