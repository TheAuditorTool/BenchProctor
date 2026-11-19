// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00863(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    long _clen = 0;
    const char *_cl = getenv("CONTENT_LENGTH");
    if (_cl != NULL) _clen = strtol(_cl, NULL, 10);
    if (_clen > 0) {
        size_t _rn = (size_t)_clen < sizeof(user_input_buf) - 1 ? (size_t)_clen : sizeof(user_input_buf) - 1;
        size_t _got = fread(user_input_buf, 1, _rn, stdin);
        user_input_buf[_got] = '\0';
    }
    const char *user_input = user_input_buf;
    char data[512];
    size_t _li = 0;
    for (; user_input[_li] != '\0' && _li < sizeof(data) - 1; ++_li) data[_li] = user_input[_li];
    data[_li] = '\0';
    char _buf[16] = "fixedcontent12";
    char _out[256];
    size_t _span = (size_t)strtoul(data, NULL, 10);
    if (_span > sizeof(_out)) _span = sizeof(_out);
    memcpy(_out, _buf, _span);
    printf("%.*s\n", (int)_span, _out);
}
