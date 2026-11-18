// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::response::IntoResponse;
use std::collections::HashMap;

pub async fn benchmark_test_00318(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    axum::response::Redirect::to(field_value.as_str()).into_response()
}
