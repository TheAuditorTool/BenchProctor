// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::response::IntoResponse;
use std::collections::HashMap;

pub async fn benchmark_test_00485(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let captured = field_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let processed = html_escape::encode_text(&data).to_string();
    return ([("content-type", "text/html")], format!("<div>{}</div>", processed)).into_response();
}
