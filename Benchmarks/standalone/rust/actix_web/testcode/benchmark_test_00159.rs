// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00159")]
pub async fn benchmark_test_00159() -> HttpResponse {
    let msg_value = crate::shared::queue_get_message("app-events");
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", msg_value).ok();
    crate::shared::db_query(&format!("SELECT * FROM users WHERE id = '{}'", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
