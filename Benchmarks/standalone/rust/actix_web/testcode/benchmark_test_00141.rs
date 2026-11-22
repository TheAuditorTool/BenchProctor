// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00141")]
pub async fn benchmark_test_00141(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let (payload, _origin) = (ua_value.clone(), "http");
    let data = payload;
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", data));
}
