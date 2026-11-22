// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00162(body: Bytes) -> impl IntoResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(xml_value.clone());
    let base = std::path::Path::new("/var/app/data");
    let candidate = tokio::fs::canonicalize(base.join(&data)).await.unwrap_or_default();
    if !candidate.starts_with(base) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let checked_path = candidate.to_string_lossy().to_string();
    let _ = tokio::fs::read_to_string(&checked_path).await;
    Json(serde_json::json!({"count": 0})).into_response()
}
