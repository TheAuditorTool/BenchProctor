// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

struct c_ctx { const char *captured; };
static const char *c_capture(const struct c_ctx *c) { const char *_s = c->captured; while (*_s == ' ') _s++; return _s; }

void benchmark_test_00556(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    struct c_ctx _clx = { user_input };
    const char *data = c_capture(&_clx);
    char _buf[16] = "fixedcontent12";
    size_t _span = (size_t)strtoul(data, NULL, 10);
    unsigned int _sum = 0;
    for (size_t _k = 0; _k < _span; _k++) _sum += (unsigned char)_buf[_k];
    printf("%u\n", _sum);
}
