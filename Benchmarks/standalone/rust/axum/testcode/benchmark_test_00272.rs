// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::response::IntoResponse;
use axum::response::Json;
use rand::rngs::SysRng;
use std::collections::HashMap;

pub async fn benchmark_test_00272(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let transform = |v: String| v.trim().to_string();
    let data = transform(field_value.clone());
    use rand::TryRng;
    let _token: u64 = SysRng.try_next_u64().expect("OS randomness unavailable");
    crate::shared::store_session(&format!("csrf_token:{}", data), &_token.to_string());
    Json(serde_json::json!({"count": 0})).into_response()
}
