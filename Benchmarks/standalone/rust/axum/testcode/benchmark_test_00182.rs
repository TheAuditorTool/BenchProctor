// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;

pub async fn benchmark_test_00182(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let captured = field_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    crate::shared::db_query(&format!("SELECT * FROM `{}`", data.replace('`', "")));
    Json(serde_json::json!({"count": 0})).into_response()
}
