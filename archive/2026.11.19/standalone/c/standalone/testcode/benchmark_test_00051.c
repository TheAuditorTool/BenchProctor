// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <libgen.h>

struct c_ctx { const char *captured; };
static const char *c_capture(const struct c_ctx *c) { const char *_s = c->captured; while (*_s == ' ') _s++; return _s; }

void benchmark_test_00051(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    if (fgets(user_input_buf, sizeof(user_input_buf), stdin) == NULL) user_input_buf[0] = '\0';
    user_input_buf[strcspn(user_input_buf, "\n")] = '\0';
    const char *user_input = user_input_buf;
    struct c_ctx _clx = { user_input };
    const char *data = c_capture(&_clx);
    char _bn_copy[512];
    snprintf(_bn_copy, sizeof(_bn_copy), "%s", data);
    const char *safe = basename(_bn_copy);
    FILE *_f = fopen(safe, "w");
    if (_f) fclose(_f);
}
