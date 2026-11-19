// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00294(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    const char *data = c_passthrough(user_input);
    char *_found = strchr(data, '=');
    if (_found != NULL) printf("%c\n", *_found);
}
