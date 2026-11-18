// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00564")]
pub async fn benchmark_test_00564() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", comment_value).ok();
    crate::shared::db_query(&format!("SELECT * FROM `{}`", data.replace('`', "")));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
