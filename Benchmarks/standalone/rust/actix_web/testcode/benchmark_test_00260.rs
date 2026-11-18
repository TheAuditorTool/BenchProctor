// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00260")]
pub async fn benchmark_test_00260() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let captured = comment_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", data));
}
