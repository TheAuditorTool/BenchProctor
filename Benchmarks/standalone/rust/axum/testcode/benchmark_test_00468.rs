// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;

pub async fn benchmark_test_00468(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let data = urlencoding::decode(&path_value).unwrap_or_default().to_string();
    return ([("content-type", "text/html")], format!("<div>{}</div>", html_escape::encode_text(&data))).into_response();
}
