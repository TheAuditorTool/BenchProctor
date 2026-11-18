// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00043(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let data = path_value.replace("\t", " ");
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.#~\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = data.clone();
    let _ = tokio::fs::read_to_string(format!("/var/app/data/{}", processed)).await;
    Json(serde_json::json!({"count": 0})).into_response()
}
