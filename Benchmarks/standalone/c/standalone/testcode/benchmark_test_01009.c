// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_01009(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    char *_p = malloc(16);
    if (_p == NULL) return;
    strcpy(_p, "pending");
    printf("%s\n", _p);
    _p = malloc(strlen(user_input) + 1);
    if (_p == NULL) return;
    strcpy(_p, user_input);
    printf("%s\n", _p);
    free(_p);
}
