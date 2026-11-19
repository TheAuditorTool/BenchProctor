// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <curl/curl.h>

void benchmark_test_00509(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    const char *safe = user_input;
    if (strncmp(user_input, "https://api.internal.svc/", 25) != 0 && strncmp(user_input, "https://cdn.internal.svc/", 25) != 0) safe = "https://api.internal.svc/data";
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_URL, safe);
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
}
