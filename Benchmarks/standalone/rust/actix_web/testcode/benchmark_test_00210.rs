// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00210")]
pub async fn benchmark_test_00210(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", user_id)).await;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
