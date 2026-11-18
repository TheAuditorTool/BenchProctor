// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00375")]
pub async fn benchmark_test_00375(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let data = String::from_utf8_lossy(&hex::decode(&user_id).unwrap_or_default()).to_string();
    Command::new("bash").arg("-c").arg(format!("echo {}", data)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
