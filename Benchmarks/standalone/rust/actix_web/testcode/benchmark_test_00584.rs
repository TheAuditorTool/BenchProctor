// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00584")]
pub async fn benchmark_test_00584(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = ua_value.replace("\t", " ");
    let processed = ammonia::clean(&data);
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", processed));
}
