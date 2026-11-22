// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00233")]
pub async fn benchmark_test_00233(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let (payload, _origin) = (ua_value.clone(), "http");
    let data = payload;
    let _cookie = actix_web::cookie::Cookie::build("session", data.clone()).http_only(true).same_site(actix_web::cookie::SameSite::Strict).finish();
    return HttpResponse::Ok().cookie(_cookie).json(serde_json::json!({"stored": true}));
}
