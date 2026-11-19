// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00762(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    const int _unit_cents = 1999;
    int _qty = atoi(user_input);
    int _total = _qty * _unit_cents;
    printf("total=%d\n", _total);
}
