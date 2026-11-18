// SPDX-License-Identifier: Apache-2.0
use axum::http::StatusCode;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00274(mut multipart: axum::extract::Multipart) -> impl IntoResponse {
    let upload_name = {
        let mut _fname = String::new();
        while let Ok(Some(_field)) = multipart.next_field().await {
            if let Some(_f) = _field.file_name() { _fname = _f.to_string(); break; }
        }
        _fname
    };
    let data = upload_name.replace("\t", " ");
    let base_dir = "/var/app/data";
    let full_path = tokio::fs::canonicalize(format!("{}/{}", base_dir, data)).await.unwrap_or_default();
    if !full_path.starts_with(base_dir) { return (StatusCode::FORBIDDEN, "").into_response(); }
    let checked_path = full_path.to_string_lossy().to_string();
    tokio::fs::remove_file(&checked_path).await.ok();
    Json(serde_json::json!({"count": 0})).into_response()
}
