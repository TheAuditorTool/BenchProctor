// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00587(headers: HeaderMap) -> impl IntoResponse {
    let auth_header = headers.get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = auth_header.replace("\t", " ");
    if !["config.json", "index.html", "readme.md"].contains(&data.as_str()) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let checked_path = format!("/var/app/data/{}", data);
    tokio::fs::write(&checked_path, "data").await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
