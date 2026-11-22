// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00300")]
pub async fn benchmark_test_00300(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let mut pending: std::collections::VecDeque<String> = field_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    return HttpResponse::Ok().insert_header((actix_web::http::header::SET_COOKIE, format!("session={}; HttpOnly; SameSite=Strict", urlencoding::encode(&data)))).json(serde_json::json!({"stored": true}));
}
