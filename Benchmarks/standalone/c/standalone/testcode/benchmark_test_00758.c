// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00758(int argc, char **argv)
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
    size_t _len = strlen(user_input);
    size_t _w = 0;
    while (_w < _len && _w < sizeof(data) - 1) { data[_w] = user_input[_w]; ++_w; }
    data[_w] = '\0';
    const size_t _rec_size = 64;
    long _count = strtol(data, NULL, 10);
    if (_count <= 0 || _count > 65536) return;
    size_t _bytes = (size_t)_count * _rec_size;
    char *_recs = malloc(_bytes);
    if (_recs) free(_recs);
}
