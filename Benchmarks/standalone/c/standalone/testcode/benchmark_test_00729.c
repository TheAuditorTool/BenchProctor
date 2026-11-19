// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <curl/curl.h>

void benchmark_test_00729(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    char data[512];
    snprintf(data, sizeof(data), "%s", user_input);
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_URL, data);
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
}
