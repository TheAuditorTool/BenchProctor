// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00261")]
pub async fn benchmark_test_00261() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    struct FormData { payload: String }
    let data = FormData { payload: db_value.clone() }.payload;
    crate::shared::set_cookie(&format!("session={}; HttpOnly; SameSite=Strict", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
