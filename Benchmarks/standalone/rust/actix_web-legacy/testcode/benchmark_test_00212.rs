// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00212/{id}")]
pub async fn benchmark_test_00212(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    let data = urlencoding::decode(&path_value).unwrap_or_default().to_string();
    use sha2::Digest;
    let mut _hasher = sha2::Sha256::new();
    _hasher.update(data.as_bytes());
    let _ = _hasher.finalize();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
