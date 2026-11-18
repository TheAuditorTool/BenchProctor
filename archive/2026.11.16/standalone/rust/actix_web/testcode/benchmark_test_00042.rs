// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00042/{id}")]
pub async fn benchmark_test_00042(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    let data: String = path_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| path_value.clone());
    tokio::fs::write(format!("/var/app/data/{}", data), "data").await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
