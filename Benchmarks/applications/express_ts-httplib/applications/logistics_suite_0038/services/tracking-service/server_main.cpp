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

void poll_tracking(const httplib::Request &, httplib::Response &);
void validate_profile(const httplib::Request &, httplib::Response &);
void prune_label(const httplib::Request &, httplib::Response &);
void enrich_header(const httplib::Request &, httplib::Response &);
void compact_shipment(const httplib::Request &, httplib::Response &);
void enrich_summary(const httplib::Request &, httplib::Response &);
void reconcile_config(const httplib::Request &, httplib::Response &);

int main()
{
    httplib::Server svr;
    svr.Get("/health", [](const httplib::Request &, httplib::Response &res) { res.set_content("ok", "text/plain"); });
    svr.Post("/poll_tracking", &poll_tracking);
    svr.Post("/validate_profile/:id", &validate_profile);
    svr.Post("/prune_label", &prune_label);
    svr.Post("/enrich_header", &enrich_header);
    svr.Post("/compact_shipment", &compact_shipment);
    svr.Post("/enrich_summary", &enrich_summary);
    svr.Post("/reconcile_config", &reconcile_config);
    const char *_port_env = std::getenv("PORT");
    int _port = _port_env ? std::atoi(_port_env) : 8080;
    svr.listen("0.0.0.0", _port);
    return 0;
}
