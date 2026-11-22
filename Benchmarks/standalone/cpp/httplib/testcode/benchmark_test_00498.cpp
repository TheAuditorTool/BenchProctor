// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>
#include <unistd.h>
#include <regex>
#include <functional>
#include <unordered_map>

namespace httplib {
struct Request {
    std::string get_param_value(const std::string &key) const;
    std::string get_header_value(const std::string &key) const;
    std::unordered_map<std::string, std::string> path_params;
    std::string body;
};
struct DataSink {
    std::function<bool(const char *, size_t)> write;
    std::function<void()> done;
};
struct Response {
    void set_content(const std::string &s, const std::string &type);
    void set_header(const std::string &key, const std::string &val);
    void set_redirect(const std::string &url, int status);
    void set_chunked_content_provider(const std::string &content_type, std::function<bool(size_t, DataSink &)> provider) { std::string _chunks; DataSink _sink; _sink.write = [&_chunks](const char *_d, size_t _n) { _chunks.append(_d, _n); return true; }; _sink.done = [] {}; provider(0, _sink); set_content(_chunks, content_type); }
    int status;
};
struct Result {};
struct Client {
    Client(const std::string &host, int port);
    Result Post(const std::string &path, const std::string &body, const std::string &content_type);
};
}

void benchmark_test_00498(const httplib::Request &, httplib::Response &res)
{
    const char *user_input_env = std::getenv("DB_ROW_VALUE");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    static const std::regex _re("^[a-zA-Z0-9 _.#%\\-]+$");
    std::string arg = std::regex_match(user_input, _re) ? user_input : std::string("default");
    std::string _html = std::string("<div class=\"comment\" data-author=\"") + arg + "\">" + arg + "</div>";
    res.set_chunked_content_provider("text/html", [_html](size_t, httplib::DataSink &_sink) {
        _sink.write(_html.data(), _html.size());
        _sink.done();
        return true;
    });
}
