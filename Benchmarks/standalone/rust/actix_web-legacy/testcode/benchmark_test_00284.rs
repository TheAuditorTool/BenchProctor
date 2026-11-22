// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00284/{id}")]
pub async fn benchmark_test_00284(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    let data = path_value.to_string();
    tokio::fs::remove_file(format!("/var/app/data/{}", data)).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
