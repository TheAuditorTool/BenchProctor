// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00095")]
pub async fn benchmark_test_00095(body: web::Bytes) -> HttpResponse {
    let graphql_var = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("variables").and_then(|vs| vs.get("input")).and_then(|i| i.as_str()).map(|s| s.to_string())).unwrap_or_default();
    struct FormData { payload: String }
    let data = FormData { payload: graphql_var.clone() }.payload;
    use md5::Digest;
    let mut _hasher = md5::Md5::new();
    _hasher.update(data.as_bytes());
    let _ = _hasher.finalize();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
