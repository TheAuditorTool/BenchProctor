// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00007")]
pub async fn benchmark_test_00007() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    HttpResponse::Found().append_header(("Location", comment_value.as_str())).finish()
}
