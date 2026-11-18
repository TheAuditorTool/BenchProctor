// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00076")]
pub async fn benchmark_test_00076(req: HttpRequest) -> HttpResponse {
    let host_value = req.headers().get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    struct FormData { payload: String }
    let data = FormData { payload: host_value.clone() }.payload;
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", data)).await;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
