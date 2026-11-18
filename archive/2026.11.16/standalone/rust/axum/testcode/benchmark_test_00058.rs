// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;

pub async fn benchmark_test_00058() -> impl IntoResponse {
    let api_value = crate::shared::fetch_url("https://api.partner.example.com/v1/records");
    let data = api_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    axum::response::Redirect::to(data.as_str()).into_response()
}
