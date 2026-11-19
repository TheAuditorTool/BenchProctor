// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00753(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    if (fgets(user_input_buf, sizeof(user_input_buf), stdin) == NULL) user_input_buf[0] = '\0';
    user_input_buf[strcspn(user_input_buf, "\n")] = '\0';
    const char *user_input = user_input_buf;
    char *_p = malloc(16);
    if (_p == NULL) return;
    strcpy(_p, "pending");
    printf("%s\n", _p);
    free(_p);
    _p = malloc(strlen(user_input) + 1);
    if (_p == NULL) return;
    strcpy(_p, user_input);
    printf("%s\n", _p);
    free(_p);
}
