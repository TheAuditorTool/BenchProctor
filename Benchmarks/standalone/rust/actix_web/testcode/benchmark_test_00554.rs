// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00554")]
pub async fn benchmark_test_00554(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    crate::shared::db_query(&format!("SELECT * FROM `{}`", referer_value.replace('`', "")));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
