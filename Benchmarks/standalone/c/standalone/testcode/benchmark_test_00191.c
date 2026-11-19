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

void benchmark_test_00191(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    struct c_ctx _clx = { user_input };
    const char *data = c_capture(&_clx);
    char *_p = malloc(16);
    if (_p == NULL) return;
    strcpy(_p, "pending");
    printf("%s\n", _p);
    free(_p);
    _p = malloc(strlen(data) + 1);
    if (_p == NULL) return;
    strcpy(_p, data);
    printf("%s\n", _p);
    free(_p);
}
