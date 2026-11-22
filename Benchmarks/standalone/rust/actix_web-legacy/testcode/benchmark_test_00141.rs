// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00141")]
pub async fn benchmark_test_00141(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut data = String::new();
    for token in ua_value.split(',') { data = token.to_string(); }
    let mut _env = minijinja::Environment::new();
    _env.add_template("profile.html", "<div class=\"profile-bio\">{{ bio|safe }}</div>").ok();
    let _page = _env.get_template("profile.html").and_then(|t| t.render(minijinja::context! { bio => data })).unwrap_or_default();
    return HttpResponse::Ok().content_type("text/html").body(_page);
}
