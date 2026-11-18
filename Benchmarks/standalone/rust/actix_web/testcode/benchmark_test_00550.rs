// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00550")]
pub async fn benchmark_test_00550(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    crate::shared::db_query(&format!("SELECT * FROM `{}`", auth_header.replace('`', "")));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
