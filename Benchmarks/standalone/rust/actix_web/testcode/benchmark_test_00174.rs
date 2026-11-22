// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00174")]
pub async fn benchmark_test_00174(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = auth_header.replace("\t", " ");
    if let Ok(mut _interp) = Command::new("bash").arg("-s").stdin(std::process::Stdio::piped()).spawn() {
        if let Some(mut _script) = _interp.stdin.take() {
            use tokio::io::AsyncWriteExt;
            _script.write_all(format!("echo {}\n", data).as_bytes()).await.ok();
        }
        _interp.wait().await.ok();
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
