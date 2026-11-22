// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;
use tokio::process::Command;

pub async fn benchmark_test_00073(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(path_value.clone());
    Command::new("sh").arg("-c").arg(format!("cat {}", data)).output().await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
