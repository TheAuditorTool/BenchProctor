// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00124")]
pub async fn benchmark_test_00124() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    struct FormData { payload: String }
    let data = FormData { payload: comment_value.clone() }.payload;
    let Some(at) = data.find('@') else { return HttpResponse::BadRequest().finish(); };
    let mail_domain = &data[at + 1..];
    let _ = mail_domain;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
