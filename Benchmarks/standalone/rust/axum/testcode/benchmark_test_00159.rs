// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00159(headers: HeaderMap) -> impl IntoResponse {
    let referer_value = headers.get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let (payload, _origin) = (referer_value.clone(), "http");
    let data = payload;
    let _bounded = data.parse::<i64>().unwrap_or(0).clamp(0, 2147483647);
    let processed = _bounded.to_string();
    let rows: u32 = processed.parse().unwrap_or(0);
    let Some(_capacity) = rows.checked_mul(512).filter(|bytes| *bytes <= 1 << 21) else { return (StatusCode::BAD_REQUEST, "").into_response(); };
    let _records: Vec<u8> = Vec::with_capacity(_capacity as usize);
    Json(serde_json::json!({"count": 0})).into_response()
}
