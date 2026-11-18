// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use base64::Engine;
use base64::engine::general_purpose;

#[actix_web::post("/benchmark_test_00440")]
pub async fn benchmark_test_00440(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = String::from_utf8_lossy(&general_purpose::STANDARD.decode(&auth_header).unwrap_or_default()).to_string();
    crate::shared::xpath_eval(&format!("//user[@id='{}']", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
