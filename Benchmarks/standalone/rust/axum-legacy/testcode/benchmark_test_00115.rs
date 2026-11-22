// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00115(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let captured = path_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let _cookie = cookie::Cookie::build(("session", data.clone())).secure(true).http_only(true).same_site(cookie::SameSite::Strict).build();
    return (axum::response::AppendHeaders([(axum::http::header::SET_COOKIE, _cookie.to_string())]), Json(serde_json::json!({"count": 0}))).into_response();
}
