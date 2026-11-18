// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;

pub async fn benchmark_test_00061() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(env_value.clone());
    axum::response::Redirect::to(data.as_str()).into_response()
}
