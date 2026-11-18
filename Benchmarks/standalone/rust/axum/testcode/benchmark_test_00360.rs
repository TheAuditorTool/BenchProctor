// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00360(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", path_value).ok();
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.%\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return (StatusCode::BAD_REQUEST, "").into_response(); }
    let processed = data.clone();
    Command::new("sh").arg("-c").arg(format!("cat {}", processed)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
