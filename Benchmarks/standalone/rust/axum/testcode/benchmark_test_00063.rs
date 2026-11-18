// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::response::IntoResponse;
use axum::response::Json;
use rand::rngs::OsRng;
use std::collections::HashMap;

pub async fn benchmark_test_00063(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let transform = |v: String| v.trim().to_string();
    let data = transform(field_value.clone());
    use rand::Rng;
    let _token: u64 = OsRng.gen();
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    Json(serde_json::json!({"count": 0})).into_response()
}
