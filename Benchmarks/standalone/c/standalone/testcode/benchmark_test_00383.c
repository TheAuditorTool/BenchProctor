// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00383(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("QUERY_STRING");
    if (user_input == NULL) user_input = "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    for (char *_r = data; *_r; ++_r) if (*_r == '\n') *_r = ' ';
    char _buf[16] = "fixedcontent12";
    char _out[256];
    size_t _span = (size_t)strtoul(data, NULL, 10);
    if (_span > sizeof(_buf)) _span = sizeof(_buf);
    memcpy(_out, _buf, _span);
    printf("%.*s\n", (int)_span, _out);
}
