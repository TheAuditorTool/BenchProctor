// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00220(int argc, char **argv)
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
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    char *_dst = malloc(16);
    if (_dst == NULL) return;
    size_t _n = strlen(data);
    if (_n > 15) _n = 15;
    memcpy(_dst, data, _n);
    _dst[_n] = '\0';
    printf("%s\n", _dst);
    free(_dst);
}
