// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use base64::Engine;
use base64::engine::general_purpose;

#[actix_web::post("/benchmark_test_00520")]
pub async fn benchmark_test_00520(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&cookie_value).unwrap_or_default()).to_string();
    crate::shared::set_cookie(&format!("session={}; Secure; HttpOnly; SameSite=Strict", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
