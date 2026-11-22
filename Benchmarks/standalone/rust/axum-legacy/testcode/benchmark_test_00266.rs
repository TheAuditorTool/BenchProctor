// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00266(headers: HeaderMap) -> impl IntoResponse {
    let auth_header = headers.get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    struct FormData { payload: String }
    let data = FormData { payload: auth_header.clone() }.payload;
    let rows: u32 = data.parse().unwrap_or(0);
    let _records: Vec<u8> = Vec::with_capacity((rows * 512) as usize);
    Json(serde_json::json!({"count": 0})).into_response()
}
