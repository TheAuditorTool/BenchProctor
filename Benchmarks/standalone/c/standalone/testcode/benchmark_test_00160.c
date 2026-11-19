// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <regex.h>

void benchmark_test_00160(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    FILE *_src_fp = fopen("/tmp/data", "r");
    if (_src_fp != NULL) {
        if (fgets(user_input_buf, sizeof(user_input_buf), _src_fp) == NULL) user_input_buf[0] = '\0';
        fclose(_src_fp);
    }
    const char *user_input = user_input_buf;
    regex_t _re;
    const char *safe = user_input;
    if (regcomp(&_re, "^[a-zA-Z0-9 %._-]+$", REG_EXTENDED) == 0) {
        if (regexec(&_re, user_input, 0, NULL, 0) != 0) safe = "config";
        regfree(&_re);
    }
    char _cmd[512];
    snprintf(_cmd, sizeof(_cmd), "grep %s /var/log/app.log", safe);
    FILE *_p = popen(_cmd, "r");
    if (_p) pclose(_p);
}
