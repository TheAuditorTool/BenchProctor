// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00317")]
pub async fn benchmark_test_00317(body: web::Bytes) -> HttpResponse {
    let json_value = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("payload").and_then(|p| p.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let (payload, _origin) = (json_value.clone(), "http");
    let data = payload;
    crate::shared::db_query_bind("SELECT * FROM users WHERE id = $1", &data);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
