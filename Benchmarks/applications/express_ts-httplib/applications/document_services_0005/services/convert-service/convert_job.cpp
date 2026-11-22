// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <unistd.h>
#include <unordered_map>
#include <regex>
#include <cctype>
#include <functional>

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

void run_conversion(const httplib::Request &req, httplib::Response &res)
{
    std::string subtitle;
    {
        const std::string &_body = req.body;
        std::string::size_type _k = _body.find("\"documents_payload\"");
        std::string::size_type _c = _k == std::string::npos ? _k : _body.find(':', _k);
        std::string::size_type _s = _c == std::string::npos ? _c : _body.find('"', _c);
        if (_s != std::string::npos) {
            std::string::size_type _e = _body.find('"', ++_s);
            if (_e != std::string::npos) subtitle = _body.substr(_s, _e - _s);
        }
    }
    std::string dossier = std::regex_match(subtitle, std::regex("^(plain|markdown|html|text)$")) ? subtitle : std::string("plain");
    std::string _html = std::string("<div class=\"comment\" data-author=\"") + dossier + "\">" + dossier + "</div>";
    res.set_chunked_content_provider("text/html", [_html](size_t, httplib::DataSink &_sink) {
        _sink.write(_html.data(), _html.size());
        _sink.done();
        return true;
    });
}
