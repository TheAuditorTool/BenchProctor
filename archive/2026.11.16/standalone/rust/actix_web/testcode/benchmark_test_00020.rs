// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00020")]
pub async fn benchmark_test_00020() -> HttpResponse {
    let msg_value = crate::shared::queue_get_message("app-events");
    let captured = msg_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    crate::shared::db_query(&format!("SELECT * FROM users WHERE id = '{}'", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
