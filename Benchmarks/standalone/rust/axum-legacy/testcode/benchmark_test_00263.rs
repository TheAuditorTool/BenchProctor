// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00263(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    struct FormData { payload: String }
    let data = FormData { payload: path_value.clone() }.payload;
    let result: Option<String> = std::env::var(data.as_str()).ok();
    let value = match result { Some(v) => v, None => return (StatusCode::NOT_FOUND, "").into_response() };
    let _ = value;
    Json(serde_json::json!({"count": 0})).into_response()
}
