// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00214(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    srand48((long)time(NULL));
    long _token = lrand48();
    printf("token for %s: %ld\n", data, _token);
}
