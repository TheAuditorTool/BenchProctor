// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00056")]
pub async fn benchmark_test_00056(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = if ua_value.len() <= 4096 { ua_value.clone() } else { ua_value.chars().take(4096).collect() };
    if let Ok(mut _interp) = Command::new("bash").arg("-s").stdin(std::process::Stdio::piped()).spawn() {
        if let Some(mut _script) = _interp.stdin.take() {
            use tokio::io::AsyncWriteExt;
            _script.write_all(format!("echo {}\n", data).as_bytes()).await.ok();
        }
        _interp.wait().await.ok();
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
