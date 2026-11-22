// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00281")]
pub async fn benchmark_test_00281() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let data = db_value.to_string();
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", data));
}
