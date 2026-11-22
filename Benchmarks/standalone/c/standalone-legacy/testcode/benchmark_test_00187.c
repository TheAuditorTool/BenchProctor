// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <curl/curl.h>

struct c_ctx { const char *captured; };
static const char *c_capture(const struct c_ctx *c) { const char *_s = c->captured; while (*_s == ' ') _s++; return _s; }

void benchmark_test_00187(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    struct c_ctx _clx = { user_input };
    const char *data = c_capture(&_clx);
    const char *arg = data;
    if (strncmp(data, "https://api.internal.svc/", 25) != 0 && strncmp(data, "https://cdn.internal.svc/", 25) != 0) arg = "https://api.internal.svc/data";
    CURLU *_u = curl_url();
    curl_url_set(_u, CURLUPART_URL, arg, 0);
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_CURLU, _u);
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
    curl_url_cleanup(_u);
}
