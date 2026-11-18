// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::response::IntoResponse;
use std::collections::HashMap;

pub async fn benchmark_test_00331(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let data: String = field_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| field_value.clone());
    axum::response::Redirect::to(data.as_str()).into_response()
}
