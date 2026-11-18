// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;

pub async fn benchmark_test_00031(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let _prefix: String = field_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => field_value.to_lowercase(),
        "f" => field_value.to_uppercase(),
        _ => field_value.trim().to_string(),
    };
    let _coerced = matches!(data.to_lowercase().as_str(), "true" | "1" | "yes" | "on");
    let processed = _coerced.to_string();
    crate::shared::xpath_eval(&format!("//user[@id='{}']", processed));
    Json(serde_json::json!({"count": 0})).into_response()
}
