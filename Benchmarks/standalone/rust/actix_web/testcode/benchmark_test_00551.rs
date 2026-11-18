// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00551")]
pub async fn benchmark_test_00551(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let data: String = xml_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| xml_value.clone());
    if !["config.json", "index.html", "readme.md"].contains(&data.as_str()) { return HttpResponse::Forbidden().finish(); }
    let checked_path = format!("/var/app/data/{}", data);
    tokio::fs::write(&checked_path, "data").await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
