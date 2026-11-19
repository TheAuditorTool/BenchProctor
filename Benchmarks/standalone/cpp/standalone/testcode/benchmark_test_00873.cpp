// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <regex>

typedef void CURL;
extern "C" CURL *curl_easy_init(void);
extern "C" int curl_easy_setopt(CURL *, int, ...);
extern "C" int curl_easy_perform(CURL *);
extern "C" void curl_easy_cleanup(CURL *);
enum { CURLOPT_URL = 10002, CURLOPT_SSL_VERIFYPEER = 64, CURLOPT_SSL_VERIFYHOST = 81, CURLOPT_SSL_VERIFYSTATUS = 232, CURLOPT_POSTFIELDS = 10015, CURLOPT_CUSTOMREQUEST = 10036, CURLOPT_WRITEFUNCTION = 20011, CURLOPT_WRITEDATA = 10001 };

void benchmark_test_00873(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_X_CUSTOM_HEADER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string _raw = user_input;
    auto _closure = [&_raw]() { std::string::size_type _e = _raw.find_last_not_of(" \t\r\n"); return _e == std::string::npos ? _raw : _raw.substr(0, _e + 1); };
    std::string data = _closure();
    std::string _authority = data;
    std::string::size_type _scheme = _authority.find("://");
    if (_scheme != std::string::npos) _authority = _authority.substr(_scheme + 3);
    else if (_authority.rfind("//", 0) == 0) _authority = _authority.substr(2);
    _authority = _authority.substr(0, _authority.find_first_of("/?#"));
    std::string::size_type _userinfo = _authority.rfind('@');
    if (_userinfo != std::string::npos) _authority = _authority.substr(_userinfo + 1);
    _authority = _authority.substr(0, _authority.find(':'));
    static const std::regex _hw("^(api\\.internal\\.example\\.com|cdn\\.internal\\.example\\.com)$");
    if (!std::regex_match(_authority, _hw)) return;
    std::string safe = data;
    std::string _hurl = safe;
    CURL *_curl = curl_easy_init();
    curl_easy_setopt(_curl, CURLOPT_URL, _hurl.c_str());
    curl_easy_perform(_curl);
    curl_easy_cleanup(_curl);
}
