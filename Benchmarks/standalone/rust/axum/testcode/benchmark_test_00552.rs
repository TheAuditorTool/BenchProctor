// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;

pub async fn benchmark_test_00552() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let data = env_value.replace("\t", " ");
    axum::response::Redirect::to(data.as_str()).into_response()
}
