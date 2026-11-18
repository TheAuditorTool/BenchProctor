// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00042")]
pub async fn benchmark_test_00042() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let captured = db_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", data));
}
