// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <curl/curl.h>

void benchmark_test_00172(int argc, char **argv)
{
    (void)argc; (void)argv;
    const char *user_input = getenv("DB_ROW_VALUE");
    if (user_input == NULL) user_input = "";
    const char *data = (strlen(user_input) > 0) ? user_input : "";
    CURLU *_u = curl_url();
    curl_url_set(_u, CURLUPART_URL, data, 0);
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_CURLU, _u);
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
    curl_url_cleanup(_u);
}
