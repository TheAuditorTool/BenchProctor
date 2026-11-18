// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00022(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    FILE *_src_fp = fopen("/etc/app/config", "r");
    if (_src_fp != NULL) {
        if (fgets(user_input_buf, sizeof(user_input_buf), _src_fp) == NULL) user_input_buf[0] = '\0';
        fclose(_src_fp);
    }
    const char *user_input = user_input_buf;
    char data[512];
    switch (user_input[0]) {
        case '\0':
            data[0] = '\0';
            break;
        default:
            snprintf(data, sizeof(data), "%s", user_input);
            break;
    }
    char _path[512];
    snprintf(_path, sizeof(_path), "/var/app/data/%s", data);
    FILE *_f = fopen(_path, "w");
    if (_f) fclose(_f);
}
