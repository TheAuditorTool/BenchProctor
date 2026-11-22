// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::response::IntoResponse;
use axum::response::Json;
use rand::rngs::SysRng;
use std::collections::HashMap;

pub async fn benchmark_test_00052(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    use rand::Rng;
    let mut _rng: rand::rngs::StdRng = rand::make_rng();
    let _token = _rng.next_u64();
    crate::shared::store_session(&format!("csrf_token:{}", field_value), &_token.to_string());
    Json(serde_json::json!({"count": 0})).into_response()
}
