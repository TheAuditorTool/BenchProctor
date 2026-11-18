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

void shop_rate(const httplib::Request &, httplib::Response &);
void archive_config(const httplib::Request &, httplib::Response &);
void collect_label(const httplib::Request &, httplib::Response &);
void load_header(const httplib::Request &, httplib::Response &);
void prune_shipment(const httplib::Request &, httplib::Response &);
void build_snapshot(const httplib::Request &, httplib::Response &);
void archive_snapshot(const httplib::Request &, httplib::Response &);
void enrich_carrier(const httplib::Request &, httplib::Response &);

int main()
{
    httplib::Server svr;
    svr.Get("/health", [](const httplib::Request &, httplib::Response &res) { res.set_content("ok", "text/plain"); });
    svr.Post("/shop_rate", &shop_rate);
    svr.Post("/archive_config", &archive_config);
    svr.Post("/collect_label", &collect_label);
    svr.Post("/load_header", &load_header);
    svr.Post("/prune_shipment", &prune_shipment);
    svr.Post("/build_snapshot", &build_snapshot);
    svr.Post("/archive_snapshot", &archive_snapshot);
    svr.Post("/enrich_carrier", &enrich_carrier);
    const char *_port_env = std::getenv("PORT");
    int _port = _port_env ? std::atoi(_port_env) : 8080;
    svr.listen("0.0.0.0", _port);
    return 0;
}
