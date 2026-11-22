// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00187")]
pub async fn benchmark_test_00187() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = match comment_value.chars().next() { Some(_) => comment_value.clone(), None => "default".to_string() };
    return HttpResponse::Ok().insert_header((actix_web::http::header::SET_COOKIE, format!("session={}; HttpOnly; SameSite=Strict", urlencoding::encode(&data)))).json(serde_json::json!({"stored": true}));
}
