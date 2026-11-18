// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00018(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("QUERY_STRING");
    if (user_input == NULL) user_input = "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    for (char *_r = data; *_r; ++_r) if (*_r == '\n') *_r = ' ';
    char _buf[16] = "fixedcontent12";
    size_t _len = (size_t)strtoul(data, NULL, 10);
    unsigned int _sum = 0;
    for (size_t _k = 0; _k < _len; _k++) _sum += (unsigned char)_buf[_k];
    printf("%u\n", _sum);
}
