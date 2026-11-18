// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00169")]
pub async fn benchmark_test_00169(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = urlencoding::decode(&referer_value).unwrap_or_default().to_string();
    let processed = ammonia::clean(&data);
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", processed));
}
