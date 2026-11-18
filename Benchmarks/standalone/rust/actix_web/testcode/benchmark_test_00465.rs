// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00465")]
pub async fn benchmark_test_00465(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let (payload, _origin) = (field_value.clone(), "http");
    let data = payload;
    crate::shared::db_query(&format!("SELECT * FROM `{}`", data.replace('`', "")));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
