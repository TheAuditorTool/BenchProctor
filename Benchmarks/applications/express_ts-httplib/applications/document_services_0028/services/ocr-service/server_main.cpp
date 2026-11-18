#include <iostream>
#include <string>
#include <unordered_map>
#include <functional>
#include <vector>
#include <utility>
#include <cstdlib>

namespace httplib {
struct Request {
    std::string get_param_value(const std::string &key) const;
    std::string get_header_value(const std::string &key) const;
    std::unordered_map<std::string, std::string> path_params;
    std::string body;
};
struct Response {
    void set_content(const std::string &s, const std::string &type);
    void set_header(const std::string &key, const std::string &val);
    void set_redirect(const std::string &url, int status);
    int status;
};
struct Result {};
struct Client {
    Client(const std::string &host, int port);
    Result Post(const std::string &path, const std::string &body, const std::string &content_type);
};
struct Server {
    typedef std::function<void(const Request &, Response &)> Handler;
    void Get(const std::string &pattern, Handler handler);
    void Post(const std::string &pattern, Handler handler);
    bool listen(const std::string &host, int port);
    std::vector<std::pair<std::string, Handler>> routes_;
};
}

void extract_text(const httplib::Request &, httplib::Response &);
void publish_checkpoint(const httplib::Request &, httplib::Response &);
void annotate_schedule(const httplib::Request &, httplib::Response &);
void compact_header(const httplib::Request &, httplib::Response &);
void render_conversion(const httplib::Request &, httplib::Response &);
void render_attachment(const httplib::Request &, httplib::Response &);
void normalize_config(const httplib::Request &, httplib::Response &);

int main()
{
    httplib::Server svr;
    svr.Get("/health", [](const httplib::Request &, httplib::Response &res) { res.set_content("ok", "text/plain"); });
    svr.Post("/extract_text", &extract_text);
    svr.Post("/publish_checkpoint", &publish_checkpoint);
    svr.Post("/annotate_schedule", &annotate_schedule);
    svr.Post("/compact_header", &compact_header);
    svr.Post("/render_conversion", &render_conversion);
    svr.Post("/render_attachment", &render_attachment);
    svr.Post("/normalize_config", &normalize_config);
    const char *_port_env = std::getenv("PORT");
    int _port = _port_env ? std::atoi(_port_env) : 8080;
    svr.listen("0.0.0.0", _port);
    return 0;
}
