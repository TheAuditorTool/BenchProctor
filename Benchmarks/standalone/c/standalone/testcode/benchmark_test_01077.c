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

void benchmark_test_01077(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    struct c_ctx _clx = { user_input };
    const char *data = c_capture(&_clx);
    char _buf[16] = "fixedcontent12";
    char _out[256];
    size_t _span = (size_t)strtoul(data, NULL, 10);
    if (_span > sizeof(_buf)) _span = sizeof(_buf);
    memcpy(_out, _buf, _span);
    printf("%.*s\n", (int)_span, _out);
}
