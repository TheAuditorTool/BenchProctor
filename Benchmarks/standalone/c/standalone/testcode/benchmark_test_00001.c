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
    const char *user_input = (argc > 1) ? argv[1] : "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    for (char *_r = data; *_r; ++_r) if (*_r == '\n') *_r = ' ';
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_URL, data);
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
}
