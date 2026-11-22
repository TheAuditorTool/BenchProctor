// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <fcntl.h>
#include <libgen.h>

void benchmark_test_00020(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    char _bn_copy[512];
    snprintf(_bn_copy, sizeof(_bn_copy), "%s", user_input);
    const char *arg = basename(_bn_copy);
    int _fd = open(arg, O_RDONLY);
    if (_fd >= 0) close(_fd);
}
