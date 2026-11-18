// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00105(body: Bytes) -> impl IntoResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let data: String = xml_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| xml_value.clone());
    if !["config.json", "index.html", "readme.md"].contains(&data.as_str()) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let checked_path = format!("/var/app/data/{}", data);
    tokio::fs::write(&checked_path, "data").await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
