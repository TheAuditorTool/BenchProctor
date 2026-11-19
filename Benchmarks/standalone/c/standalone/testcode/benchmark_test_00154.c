// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00154(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    srand((unsigned)time(NULL));
    int _token = rand();
    printf("token for %s: %d\n", user_input, _token);
}
