// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00291")]
pub async fn benchmark_test_00291(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let _prefix: String = field_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => field_value.to_lowercase(),
        "f" => field_value.to_uppercase(),
        _ => field_value.trim().to_string(),
    };
    crate::shared::store_session("data", &data);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
