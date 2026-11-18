// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00406")]
pub async fn benchmark_test_00406(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    let data = String::from_utf8_lossy(&hex::decode(&cookie_value).unwrap_or_default()).to_string();
    let _coerced = matches!(data.to_lowercase().as_str(), "true" | "1" | "yes" | "on");
    let processed = _coerced.to_string();
    crate::shared::store_session("data", &processed);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
