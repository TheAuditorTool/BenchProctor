// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <regex.h>

void benchmark_test_00005(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    long _clen = 0;
    const char *_cl = getenv("CONTENT_LENGTH");
    if (_cl != NULL) _clen = strtol(_cl, NULL, 10);
    if (_clen > 0) {
        size_t _rn = (size_t)_clen < sizeof(user_input_buf) - 1 ? (size_t)_clen : sizeof(user_input_buf) - 1;
        size_t _got = fread(user_input_buf, 1, _rn, stdin);
        user_input_buf[_got] = '\0';
    }
    const char *user_input = user_input_buf;
    regex_t _re;
    const char *safe = user_input;
    if (regcomp(&_re, "^[a-zA-Z0-9 #._~-]+$", REG_EXTENDED) == 0) {
        if (regexec(&_re, user_input, 0, NULL, 0) != 0) safe = "config";
        regfree(&_re);
    }
    char _path[512];
    snprintf(_path, sizeof(_path), "/var/app/data/%s", safe);
    FILE *_f = fopen(_path, "r");
    if (_f) fclose(_f);
}
