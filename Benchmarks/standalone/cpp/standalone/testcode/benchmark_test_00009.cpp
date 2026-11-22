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
typedef struct Curl_URL CURLU;
extern "C" CURLU *curl_url(void);
extern "C" int curl_url_set(CURLU *, int, const char *, unsigned int);
extern "C" void curl_url_cleanup(CURLU *);
enum { CURLOPT_CURLU = 10282, CURLUPART_URL = 0 };

void benchmark_test_00009(int, char **)
{
    const char *user_input_env = std::getenv("MULTIPART_FIELD");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    auto _fn = [](const std::string &s) { std::string::size_type _b = s.find_first_not_of(" \t\r\n"); return _b == std::string::npos ? s : s.substr(_b); };
    std::string data = _fn(user_input);
    CURLU *_u = curl_url();
    curl_url_set(_u, CURLUPART_URL, data.c_str(), 0);
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_CURLU, _u);
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
    curl_url_cleanup(_u);
}
