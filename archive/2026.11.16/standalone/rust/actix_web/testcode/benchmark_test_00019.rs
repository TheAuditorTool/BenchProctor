// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00019")]
pub async fn benchmark_test_00019(body: web::Bytes) -> HttpResponse {
    let json_value = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("payload").and_then(|p| p.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let data = serde_json::from_str::<serde_json::Value>(&json_value)
        .ok().and_then(|v| v["value"].as_str().map(|s| s.to_string())).unwrap_or_default();
    crate::shared::db_query_bind("SELECT * FROM users WHERE id = $1", &data);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
