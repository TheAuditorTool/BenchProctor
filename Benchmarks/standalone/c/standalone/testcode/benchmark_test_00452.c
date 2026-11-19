// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <libgen.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00452(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    const char *(*_fn)(const char *) = c_passthrough;
    const char *data = _fn(user_input);
    char _bn_copy[512];
    snprintf(_bn_copy, sizeof(_bn_copy), "%s", data);
    const char *safe = basename(_bn_copy);
    remove(safe);
}
