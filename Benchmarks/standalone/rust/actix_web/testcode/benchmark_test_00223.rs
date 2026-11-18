// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00223")]
pub async fn benchmark_test_00223(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(user_id.clone());
    let _coerced = data.parse::<i64>().unwrap_or(0);
    let processed = _coerced.to_string();
    crate::shared::db_query(&format!("SELECT * FROM users WHERE id = {}", processed));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
