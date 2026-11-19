// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00115(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    const char *(*_fn)(const char *) = c_passthrough;
    const char *data = _fn(user_input);
    char _buf[16] = "fixedcontent12";
    char _out[256];
    size_t _span = (size_t)strtoul(data, NULL, 10);
    if (_span > sizeof(_buf)) _span = sizeof(_buf);
    memcpy(_out, _buf, _span);
    printf("%.*s\n", (int)_span, _out);
}
