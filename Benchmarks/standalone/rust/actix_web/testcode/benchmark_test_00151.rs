// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00151")]
pub async fn benchmark_test_00151() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data: String = db_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| db_value.clone());
    return HttpResponse::Ok().insert_header((actix_web::http::header::SET_COOKIE, format!("session={}; Secure; HttpOnly; SameSite=Strict", urlencoding::encode(&data)))).json(serde_json::json!({"stored": true}));
}
