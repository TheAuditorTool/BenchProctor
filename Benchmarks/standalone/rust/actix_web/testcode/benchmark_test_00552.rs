// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00552")]
pub async fn benchmark_test_00552(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(user_id.clone());
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = match result { Some(v) => v, None => return HttpResponse::NotFound().finish() };
    let _ = value;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
