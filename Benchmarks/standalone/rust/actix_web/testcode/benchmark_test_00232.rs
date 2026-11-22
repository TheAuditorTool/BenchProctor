// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00232/{id}")]
pub async fn benchmark_test_00232(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    crate::shared::store_session("data", &path_value);
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
