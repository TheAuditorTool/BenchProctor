// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <curl/curl.h>

static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00332(int argc, char **argv)
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
    const char *(*_fn)(const char *) = c_passthrough;
    const char *data = _fn(user_input);
    CURLU *_u = curl_url();
    curl_url_set(_u, CURLUPART_URL, data, 0);
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_CURLU, _u);
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
    curl_url_cleanup(_u);
}
