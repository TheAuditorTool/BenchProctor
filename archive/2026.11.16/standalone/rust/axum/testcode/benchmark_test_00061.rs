// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;

pub async fn benchmark_test_00061(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    crate::shared::set_cookie(&format!("session={}; HttpOnly; SameSite=Strict", field_value));
    Json(serde_json::json!({"count": 0})).into_response()
}
