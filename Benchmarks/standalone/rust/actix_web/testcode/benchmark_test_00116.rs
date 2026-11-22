// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00116")]
pub async fn benchmark_test_00116(req: HttpRequest) -> HttpResponse {
    let origin_value = req.headers().get("origin").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let _cookie = actix_web::cookie::Cookie::build("session", origin_value.clone()).secure(true).http_only(true).same_site(actix_web::cookie::SameSite::Strict).finish();
    return HttpResponse::Ok().cookie(_cookie).json(serde_json::json!({"stored": true}));
}
