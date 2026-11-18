// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00133")]
pub async fn benchmark_test_00133(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    struct FormData { payload: String }
    let data = FormData { payload: user_id.clone() }.payload;
    crate::shared::set_cookie(&format!("session={}; HttpOnly; SameSite=Strict", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
