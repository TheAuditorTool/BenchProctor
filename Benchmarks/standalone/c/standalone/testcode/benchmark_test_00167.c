// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00167(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("QUERY_STRING");
    if (user_input == NULL) user_input = "";
    const char *(*_fn)(const char *) = c_passthrough;
    const char *data = _fn(user_input);
    char _resolved[1024];
    char _joined[1024];
    snprintf(_joined, sizeof(_joined), "/var/app/data/%s", data);
    if (realpath(_joined, _resolved) == NULL) return;
    if (strncmp(_resolved, "/var/app/data/", 14) != 0) return;
    const char *safe = _resolved;
    FILE *_f = fopen(safe, "r");
    if (_f) fclose(_f);
}
