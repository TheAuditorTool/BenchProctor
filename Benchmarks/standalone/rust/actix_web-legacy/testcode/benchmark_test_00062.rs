// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00062")]
pub async fn benchmark_test_00062(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = referer_value.to_string();
    if let Ok(_target) = reqwest::Url::parse(&data) {
        let _request = reqwest::Request::new(reqwest::Method::GET, _target);
        let _client = reqwest::Client::new();
        _client.execute(_request).await.ok();
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
