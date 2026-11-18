// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00530")]
pub async fn benchmark_test_00530(body: web::Bytes) -> HttpResponse {
    let raw_body = String::from_utf8_lossy(&body).to_string();
    let mut data = String::new();
    for token in raw_body.split(',') { data = token.to_string(); }
    use diesel::prelude::*;
    if let Ok(mut conn) = diesel::SqliteConnection::establish(":memory:") {
        let _ = crate::shared::users::table.filter(crate::shared::users::name.eq(data.as_str())).load::<(i32, String)>(&mut conn);
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
