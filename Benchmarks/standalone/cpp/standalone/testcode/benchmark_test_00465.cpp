// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

typedef void CURL;
extern "C" CURL *curl_easy_init(void);
extern "C" int curl_easy_setopt(CURL *, int, ...);
extern "C" int curl_easy_perform(CURL *);
extern "C" void curl_easy_cleanup(CURL *);
enum { CURLOPT_URL = 10002, CURLOPT_SSL_VERIFYPEER = 64, CURLOPT_SSL_VERIFYHOST = 81, CURLOPT_SSL_VERIFYSTATUS = 232, CURLOPT_POSTFIELDS = 10015, CURLOPT_CUSTOMREQUEST = 10036, CURLOPT_WRITEFUNCTION = 20011, CURLOPT_WRITEDATA = 10001 };

void benchmark_test_00465(int, char **)
{
    const char *user_input_env = std::getenv("UPLOAD_FILENAME");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data = user_input;
    for (char &_c : data) if (_c == '\n') _c = ' ';
    std::string _hurl = data;
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_URL, _hurl.c_str());
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
}
