// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00035")]
pub async fn benchmark_test_00035(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let data = user_id.replace("\t", " ");
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = result.unwrap();
    let _ = value;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
