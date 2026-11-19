// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

struct c_payload { const char *value; };

void benchmark_test_00054(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    struct c_payload _pd;
    _pd.value = user_input;
    const char *data = _pd.value;
    const long _unit_cents = 1999;
    long _qty = strtol(data, NULL, 10);
    if (_qty < 0 || _qty > 100000) return;
    long _total = _qty * _unit_cents;
    printf("total=%ld\n", _total);
}
