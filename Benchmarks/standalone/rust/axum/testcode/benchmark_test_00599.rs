// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::response::IntoResponse;
use std::collections::HashMap;

pub async fn benchmark_test_00599(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let data = match field_value.chars().next() { Some(_) => field_value.clone(), None => "default".to_string() };
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
