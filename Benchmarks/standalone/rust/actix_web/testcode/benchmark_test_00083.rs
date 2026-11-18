// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00083")]
pub async fn benchmark_test_00083(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(ua_value.clone());
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", data));
}
