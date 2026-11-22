// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00081")]
pub async fn benchmark_test_00081(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
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
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
