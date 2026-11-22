// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00046")]
pub async fn benchmark_test_00046(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    use md5::Digest;
    let _ = md5::Md5::digest(user_id.as_bytes());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
