// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00421")]
pub async fn benchmark_test_00421(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let mut data = String::new();
    for token in user_id.split(',') { data = token.to_string(); }
    HttpResponse::Found().append_header(("Location", data.as_str())).finish()
}
