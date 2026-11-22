// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00032")]
pub async fn benchmark_test_00032(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let mut pending: std::collections::VecDeque<String> = referer_value.split(',').map(String::from).collect();
    let mut data = String::new();
    while let Some(item) = pending.pop_front() { data = item; }
    if let Ok(_target) = reqwest::Url::parse(&data) {
        let _request = reqwest::Request::new(reqwest::Method::GET, _target);
        let _client = reqwest::Client::new();
        _client.execute(_request).await.ok();
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
