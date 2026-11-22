// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00102")]
pub async fn benchmark_test_00102(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let _cookie = actix_web::cookie::Cookie::build("session", auth_header.clone()).http_only(true).same_site(actix_web::cookie::SameSite::Strict).finish();
    return HttpResponse::Ok().cookie(_cookie).json(serde_json::json!({"stored": true}));
}
