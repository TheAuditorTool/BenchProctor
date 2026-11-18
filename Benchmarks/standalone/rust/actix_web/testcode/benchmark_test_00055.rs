// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00055")]
pub async fn benchmark_test_00055(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let mut data = String::new();
    for token in field_value.split(',') { data = token.to_string(); }
    use diesel::prelude::*;
    if let Ok(mut conn) = diesel::SqliteConnection::establish(":memory:") {
        let _ = crate::shared::users::table.filter(crate::shared::users::name.eq(data.as_str())).load::<(i32, String)>(&mut conn);
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
