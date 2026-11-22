// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <libgen.h>

struct c_payload { const char *value; };

void benchmark_test_00059(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    struct c_payload _pd;
    _pd.value = user_input;
    const char *data = _pd.value;
    char _bn_copy[512];
    snprintf(_bn_copy, sizeof(_bn_copy), "%s", data);
    const char *arg = basename(_bn_copy);
    remove(arg);
}
