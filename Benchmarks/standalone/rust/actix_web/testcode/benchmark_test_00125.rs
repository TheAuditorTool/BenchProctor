// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00125/{id}")]
pub async fn benchmark_test_00125(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    let (payload, _origin) = (path_value.clone(), "http");
    let data = payload;
    reqwest::get(&data).await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
