// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;
use tokio::process::Command;

pub async fn benchmark_test_00072(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    let captured = field_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    if let Ok(mut _interp) = Command::new("bash").arg("-s").stdin(std::process::Stdio::piped()).spawn() {
        if let Some(mut _script) = _interp.stdin.take() {
            use tokio::io::AsyncWriteExt;
            _script.write_all(format!("echo {}\n", data).as_bytes()).await.ok();
        }
        _interp.wait().await.ok();
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
