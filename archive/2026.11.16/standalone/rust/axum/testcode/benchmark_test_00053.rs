// SPDX-License-Identifier: Apache-2.0
use axum::body::Bytes;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00053(body: Bytes) -> impl IntoResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    let _prefix: String = xml_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => xml_value.to_lowercase(),
        "f" => xml_value.to_uppercase(),
        _ => xml_value.trim().to_string(),
    };
    let checked_path = format!("/var/app/data/{}", std::path::Path::new(&data).file_name().and_then(|n| n.to_str()).unwrap_or(""));
    let _ = tokio::fs::read_to_string(&checked_path).await;
    Json(serde_json::json!({"count": 0})).into_response()
}
