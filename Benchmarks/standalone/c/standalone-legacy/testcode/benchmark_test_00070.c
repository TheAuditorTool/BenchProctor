// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <curl/curl.h>

void benchmark_test_00070(int argc, char **argv)
{
    const char *user_input = (argc > 1) ? argv[1] : "";
    char data[512];
    switch (user_input[0]) {
        case '\0':
            data[0] = '\0';
            break;
        default:
            snprintf(data, sizeof(data), "%s", user_input);
            break;
    }
    const char *arg = data;
    if (strncmp(data, "https://api.internal.svc/", 25) != 0 && strncmp(data, "https://cdn.internal.svc/", 25) != 0) arg = "https://api.internal.svc/data";
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_URL, arg);
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
}
