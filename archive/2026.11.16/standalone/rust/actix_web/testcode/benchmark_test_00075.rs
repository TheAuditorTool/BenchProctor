// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00075")]
pub async fn benchmark_test_00075(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let data = match user_id.chars().next() { Some(_) => user_id.clone(), None => "default".to_string() };
    let processed = html_escape::encode_text(&data).to_string();
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", processed));
}
