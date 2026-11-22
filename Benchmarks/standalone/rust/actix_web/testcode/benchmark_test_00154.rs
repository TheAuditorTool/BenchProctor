// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00154")]
pub async fn benchmark_test_00154(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data: String = header_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| header_value.clone());
    if let Ok(_target) = reqwest::Url::parse(&data) {
        let _request = reqwest::Request::new(reqwest::Method::GET, _target);
        let _client = reqwest::Client::new();
        _client.execute(_request).await.ok();
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
