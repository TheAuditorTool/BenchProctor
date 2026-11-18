// SPDX-License-Identifier: Apache-2.0
use axum::extract::Form;
use axum::response::IntoResponse;
use axum::response::Json;
use std::collections::HashMap;
use tokio::process::Command;

pub async fn benchmark_test_00425(Form(form): Form<HashMap<String, String>>) -> impl IntoResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", field_value).ok();
    Command::new("sh").arg("-c").arg(format!("grep {} /var/log/app.log", data)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
