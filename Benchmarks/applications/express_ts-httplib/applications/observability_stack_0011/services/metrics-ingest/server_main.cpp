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

void ingest_metric(const httplib::Request &, httplib::Response &);
void summarize_trace(const httplib::Request &, httplib::Response &);
void format_header(const httplib::Request &, httplib::Response &);
void normalize_config(const httplib::Request &, httplib::Response &);
void summarize_digest(const httplib::Request &, httplib::Response &);
void publish_checkpoint(const httplib::Request &, httplib::Response &);
void export_digest(const httplib::Request &, httplib::Response &);
void normalize_index(const httplib::Request &, httplib::Response &);

int main()
{
    httplib::Server svr;
    svr.Get("/health", [](const httplib::Request &, httplib::Response &res) { res.set_content("ok", "text/plain"); });
    svr.Post("/ingest_metric", &ingest_metric);
    svr.Post("/summarize_trace", &summarize_trace);
    svr.Post("/format_header", &format_header);
    svr.Post("/normalize_config", &normalize_config);
    svr.Post("/summarize_digest", &summarize_digest);
    svr.Post("/publish_checkpoint", &publish_checkpoint);
    svr.Post("/export_digest", &export_digest);
    svr.Post("/normalize_index", &normalize_index);
    const char *_port_env = std::getenv("PORT");
    int _port = _port_env ? std::atoi(_port_env) : 8080;
    svr.listen("0.0.0.0", _port);
    return 0;
}
