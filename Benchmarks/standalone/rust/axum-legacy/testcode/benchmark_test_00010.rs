// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;

pub async fn benchmark_test_00010() -> impl IntoResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let (payload, _origin) = (env_value.clone(), "http");
    let data = payload;
    axum::response::Redirect::temporary(data.as_str()).into_response()
}
