// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00229")]
pub async fn benchmark_test_00229(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let mut data = String::new();
    for token in xml_value.split(',') { data = token.to_string(); }
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    crate::shared::xpath_eval(&format!("//user[@id='{}']", processed));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
