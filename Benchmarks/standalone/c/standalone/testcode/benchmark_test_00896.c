// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00896(int argc, char **argv)
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
    const char *data = (strlen(user_input) > 0) ? user_input : "";
    size_t _n = strlen(data);
    char *_p = malloc(_n + 1);
    if (_p == NULL) return;
    memcpy(_p, data, _n + 1);
    printf("%s\n", _p);
    memset(_p, 0, _n + 1);
    free(_p);
}
