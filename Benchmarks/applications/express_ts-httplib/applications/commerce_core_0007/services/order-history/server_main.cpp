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

void lookup_order(const httplib::Request &, httplib::Response &);
void normalize_fulfillment(const httplib::Request &, httplib::Response &);
void fetch_roster(const httplib::Request &, httplib::Response &);
void annotate_schedule(const httplib::Request &, httplib::Response &);
void resolve_roster(const httplib::Request &, httplib::Response &);
void compact_roster(const httplib::Request &, httplib::Response &);
void compact_cart(const httplib::Request &, httplib::Response &);
void prune_receipt(const httplib::Request &, httplib::Response &);

int main()
{
    httplib::Server svr;
    svr.Get("/health", [](const httplib::Request &, httplib::Response &res) { res.set_content("ok", "text/plain"); });
    svr.Post("/lookup_order", &lookup_order);
    svr.Post("/normalize_fulfillment", &normalize_fulfillment);
    svr.Post("/fetch_roster", &fetch_roster);
    svr.Post("/annotate_schedule", &annotate_schedule);
    svr.Post("/resolve_roster", &resolve_roster);
    svr.Post("/compact_roster", &compact_roster);
    svr.Post("/compact_cart", &compact_cart);
    svr.Post("/prune_receipt", &prune_receipt);
    const char *_port_env = std::getenv("PORT");
    int _port = _port_env ? std::atoi(_port_env) : 8080;
    svr.listen("0.0.0.0", _port);
    return 0;
}
