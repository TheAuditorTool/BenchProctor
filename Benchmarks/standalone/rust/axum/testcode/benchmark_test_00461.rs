// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;
use rand::rngs::OsRng;

pub async fn benchmark_test_00461(headers: HeaderMap) -> impl IntoResponse {
    let referer_value = headers.get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", referer_value).ok();
    use rand::Rng;
    let _token: u64 = OsRng.gen();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    Json(serde_json::json!({"count": 0})).into_response()
}
