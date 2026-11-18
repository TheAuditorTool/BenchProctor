// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00034")]
pub async fn benchmark_test_00034(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let data = String::from_utf8_lossy(&hex::decode(&user_id).unwrap_or_default()).to_string();
    reqwest::get(&data).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
