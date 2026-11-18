// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00379")]
pub async fn benchmark_test_00379(body: web::Bytes) -> HttpResponse {
    let json_value = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("payload").and_then(|p| p.as_str()).map(|s| s.to_string())).unwrap_or_default();
    struct FormData { payload: String }
    let data = FormData { payload: json_value.clone() }.payload;
    crate::shared::set_cookie(&format!("session={}; HttpOnly; SameSite=Strict", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
