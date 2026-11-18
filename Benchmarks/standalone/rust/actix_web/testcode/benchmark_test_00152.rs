// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00152")]
pub async fn benchmark_test_00152(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let data = field_value.to_string();
    crate::shared::store_session("data", &data);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
