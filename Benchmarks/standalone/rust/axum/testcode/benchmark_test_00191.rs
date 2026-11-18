// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00191(body: Bytes) -> impl IntoResponse {
    let graphql_var = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("variables").and_then(|vs| vs.get("input")).and_then(|i| i.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let (payload, _origin) = (graphql_var.clone(), "http");
    let data = payload;
    if !["config.json", "index.html", "readme.md"].contains(&data.as_str()) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let checked_path = format!("/var/app/data/{}", data);
    tokio::fs::remove_file(&checked_path).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
