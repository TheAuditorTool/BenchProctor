// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;

pub async fn benchmark_test_00512(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let data = urlencoding::decode(&field_value).unwrap_or_default().to_string();
    use sha2::Digest;
    let _ = sha2::Sha256::digest(data.as_bytes());
    Json(serde_json::json!({"count": 0})).into_response()
}
