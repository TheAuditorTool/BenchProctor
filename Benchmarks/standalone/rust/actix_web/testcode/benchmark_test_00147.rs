// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00147")]
pub async fn benchmark_test_00147(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let (payload, _origin) = (user_id.clone(), "http");
    let data = payload;
    use sha2::Digest;
    let mut _hasher = sha2::Sha256::new();
    _hasher.update(data.as_bytes());
    let _ = _hasher.finalize();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
