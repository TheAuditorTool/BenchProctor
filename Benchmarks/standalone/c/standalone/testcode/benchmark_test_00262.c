// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00262(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("QUERY_STRING");
    if (user_input == NULL) user_input = "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    for (char *_r = data; *_r; ++_r) if (*_r == '\n') *_r = ' ';
    const long _unit_cents = 1999;
    long _qty = strtol(data, NULL, 10);
    if (_qty < 0 || _qty > 100000) return;
    long _total = _qty * _unit_cents;
    printf("total=%ld\n", _total);
}
