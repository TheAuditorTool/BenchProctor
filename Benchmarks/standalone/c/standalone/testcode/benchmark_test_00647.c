// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00647(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    const char *data = c_passthrough(user_input);
    const long _unit_cents = 1999;
    long _qty = strtol(data, NULL, 10);
    if (_qty < 0 || _qty > 100000) return;
    long _total = _qty * _unit_cents;
    printf("total=%ld\n", _total);
}
