// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <regex.h>

void benchmark_test_00993(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    const char *data = (strlen(user_input) > 0) ? user_input : "";
    regex_t _re;
    const char *safe = data;
    if (regcomp(&_re, "^[a-zA-Z0-9 #._~-]+$", REG_EXTENDED) == 0) {
        if (regexec(&_re, data, 0, NULL, 0) != 0) safe = "config";
        regfree(&_re);
    }
    char _path[512];
    snprintf(_path, sizeof(_path), "/var/app/data/%s", safe);
    remove(_path);
}
