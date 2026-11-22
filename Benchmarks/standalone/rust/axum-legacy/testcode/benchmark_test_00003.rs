// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00003(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", path_value).ok();
    let plan_limits: std::collections::HashMap<&str, u32> = std::collections::HashMap::from([("free", 3), ("team", 25), ("enterprise", 500)]);
    let Some(seat_limit) = plan_limits.get(data.as_str()).copied() else { return (StatusCode::NOT_FOUND, "").into_response(); };
    let _ = seat_limit;
    Json(serde_json::json!({"count": 0})).into_response()
}
