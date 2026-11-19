// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <regex.h>

void benchmark_test_00659(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    regex_t _re;
    const char *safe = user_input;
    if (regcomp(&_re, "^(asc|desc|name|created)$", REG_EXTENDED) == 0) {
        if (regexec(&_re, user_input, 0, NULL, 0) != 0) safe = "asc";
        regfree(&_re);
    }
    char _path[512];
    snprintf(_path, sizeof(_path), "/var/app/data/%s", safe);
    remove(_path);
}
