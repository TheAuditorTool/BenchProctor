// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <curl/curl.h>

void benchmark_test_00001(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    char data[512];
    size_t _len = strlen(user_input);
    size_t _w = 0;
    while (_w < _len && _w < sizeof(data) - 1) { data[_w] = user_input[_w]; ++_w; }
    data[_w] = '\0';
    const char *arg = data;
    if (strncmp(data, "https://api.internal.svc/", 25) != 0 && strncmp(data, "https://cdn.internal.svc/", 25) != 0) arg = "https://api.internal.svc/data";
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_URL, arg);
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
}
