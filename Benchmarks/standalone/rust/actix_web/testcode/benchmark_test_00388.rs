// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00388")]
pub async fn benchmark_test_00388(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(cookie_value.clone());
    tokio::fs::remove_file(format!("/var/app/data/{}", data)).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
