// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use rand::rngs::OsRng;

#[actix_web::post("/benchmark_test_00039")]
pub async fn benchmark_test_00039(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(user_id.clone());
    use rand::Rng;
    let _token: u64 = OsRng.gen();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
