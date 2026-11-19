// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00346(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    char _dst[16];
    size_t _n = strlen(data);
    if (_n >= sizeof(_dst)) _n = sizeof(_dst) - 1;
    memcpy(_dst, data, _n);
    _dst[_n] = '\0';
    printf("%s\n", _dst);
}
