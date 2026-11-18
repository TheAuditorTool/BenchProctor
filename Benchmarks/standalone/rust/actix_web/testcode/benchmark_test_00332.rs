// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00332")]
pub async fn benchmark_test_00332(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    let (payload, _origin) = (cookie_value.clone(), "http");
    let data = payload;
    use diesel::prelude::*;
    if let Ok(mut conn) = diesel::SqliteConnection::establish(":memory:") {
        let _ = crate::shared::users::table.filter(crate::shared::users::name.eq(data.as_str())).load::<(i32, String)>(&mut conn);
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
