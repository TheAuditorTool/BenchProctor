// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00226(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    if (fgets(user_input_buf, sizeof(user_input_buf), stdin) == NULL) user_input_buf[0] = '\0';
    user_input_buf[strcspn(user_input_buf, "\n")] = '\0';
    const char *user_input = user_input_buf;
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    size_t _n = strlen(data);
    char *_p = malloc(_n + 1);
    if (_p == NULL) return;
    memcpy(_p, data, _n + 1);
    printf("%s\n", _p);
    free(_p);
    memset(_p, 0, _n + 1);
}
