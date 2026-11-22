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

void benchmark_test_00423(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    const char *data = c_passthrough(user_input);
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
