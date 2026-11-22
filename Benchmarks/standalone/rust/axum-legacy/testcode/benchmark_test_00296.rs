// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;

pub async fn benchmark_test_00296(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    struct FormData { payload: String }
    let data = FormData { payload: field_value.clone() }.payload;
    let Some(at) = data.find('@') else { return (StatusCode::BAD_REQUEST, "").into_response(); };
    let mail_domain = &data[at + 1..];
    let _ = mail_domain;
    Json(serde_json::json!({"count": 0})).into_response()
}
