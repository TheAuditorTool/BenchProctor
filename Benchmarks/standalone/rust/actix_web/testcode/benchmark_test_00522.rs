// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};
use tokio::process::Command;

#[actix_web::post("/benchmark_test_00522")]
pub async fn benchmark_test_00522(web::Form(form): web::Form<std::collections::HashMap<String, String>>) -> HttpResponse {
    let field_value = form.get("field").cloned().unwrap_or_default();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(field_value.clone());
    Command::new("sh").arg("-c").arg(format!("grep {} /var/log/app.log", data)).output().await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
