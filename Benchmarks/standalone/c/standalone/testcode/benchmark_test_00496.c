// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

#define FREE_AND_NULL(_ptr) do { free(_ptr); (_ptr) = NULL; } while (0)

void benchmark_test_00496(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    char *_p = malloc(strlen(data) + 1);
    if (_p == NULL) return;
    strcpy(_p, data);
    char *_cleanup_ptr = _p;
    printf("%s\n", _p);
    FREE_AND_NULL(_p);
    _cleanup_ptr = NULL;
    if (_cleanup_ptr) free(_cleanup_ptr);
}
