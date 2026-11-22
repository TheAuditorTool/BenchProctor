// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00120")]
pub async fn benchmark_test_00120(req: HttpRequest) -> HttpResponse {
    let host_value = req.headers().get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut pending: std::collections::VecDeque<String> = host_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    use sha2::Digest;
    let mut _hasher = sha2::Sha256::new();
    _hasher.update(data.as_bytes());
    let _ = _hasher.finalize();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
