// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00078/{id}")]
pub async fn benchmark_test_00078(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    let data = match path_value.chars().next() { Some(_) => path_value.clone(), None => "default".to_string() };
    Command::new("echo").arg(&data).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
