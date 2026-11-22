// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00143")]
pub async fn benchmark_test_00143() -> HttpResponse {
    let msg_value = crate::shared::queue_get_message("app-events");
    let data = String::from_utf8_lossy(msg_value.as_bytes()).to_string();
    if let Ok(_target) = reqwest::Url::parse(&data) {
        let _request = reqwest::Request::new(reqwest::Method::GET, _target);
        let _client = reqwest::Client::new();
        _client.execute(_request).await.ok();
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
