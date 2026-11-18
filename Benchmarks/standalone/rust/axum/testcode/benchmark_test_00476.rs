// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00476() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let (payload, _origin) = (env_value.clone(), "http");
    let data = payload;
    let requested: u32 = data.parse().unwrap_or(0);
    let count = (requested * 4096) as usize;
    let _buf: Vec<u8> = vec![0u8; count];
    Json(serde_json::json!({"count": 0})).into_response()
}
