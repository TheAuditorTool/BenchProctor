// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;

pub async fn benchmark_test_00160() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", env_value).ok();
    (StatusCode::FOUND, [(axum::http::header::LOCATION, data.clone())]).into_response()
}
