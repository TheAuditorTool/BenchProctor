// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00122")]
pub async fn benchmark_test_00122(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    crate::shared::set_cookie(&format!("session={}; HttpOnly; SameSite=Strict", ua_value));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
