// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00081(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    const char *data = (strlen(user_input) > 0) ? user_input : "";
    char *_p = malloc(strlen(data) + 1);
    if (_p == NULL) return;
    strcpy(_p, data);
    if (strchr(_p, ';') != NULL) { free(_p); return; }
    printf("%s\n", _p);
    free(_p);
}
