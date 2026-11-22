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

void benchmark_test_00393(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("APP_INPUT");
    if (user_input == NULL) user_input = "";
    const char *data = c_passthrough(user_input);
    const char *arg = data;
    if (strncmp(data, "https://api.internal.svc/", 25) != 0 && strncmp(data, "https://cdn.internal.svc/", 25) != 0) arg = "https://api.internal.svc/data";
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_URL, arg);
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
}
