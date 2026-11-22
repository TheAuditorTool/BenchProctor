// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00043")]
pub async fn benchmark_test_00043(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    crate::shared::db_query(&format!("SELECT * FROM users WHERE id = '{}'", field_value));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
