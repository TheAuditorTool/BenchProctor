// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00192/{id}")]
pub async fn benchmark_test_00192(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    let mut pending: std::collections::VecDeque<String> = path_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    use md5::Digest;
    let mut _hasher = md5::Md5::new();
    _hasher.update(data.as_bytes());
    let _ = _hasher.finalize();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
