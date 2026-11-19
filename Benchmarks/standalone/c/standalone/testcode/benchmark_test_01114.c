// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

#define FREE_AND_NULL(_ptr) do { free(_ptr); (_ptr) = NULL; } while (0)

void benchmark_test_01114(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    char *_p = malloc(strlen(user_input) + 1);
    if (_p == NULL) return;
    strcpy(_p, user_input);
    char *_cleanup_ptr = _p;
    printf("%s\n", _p);
    FREE_AND_NULL(_p);
    _cleanup_ptr = NULL;
    if (_cleanup_ptr) free(_cleanup_ptr);
}
