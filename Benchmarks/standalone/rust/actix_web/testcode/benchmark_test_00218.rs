// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00218/{id}")]
pub async fn benchmark_test_00218(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(path_value.clone());
    let processed = ammonia::clean(&data);
    let mut _env = minijinja::Environment::new();
    _env.add_template("profile.html", "<div class=\"profile-bio\">{{ bio|safe }}</div>").ok();
    let _page = _env.get_template("profile.html").and_then(|t| t.render(minijinja::context! { bio => processed })).unwrap_or_default();
    return HttpResponse::Ok().content_type("text/html").body(_page);
}
