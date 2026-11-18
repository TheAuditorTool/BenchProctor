// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;

pub async fn benchmark_test_00431(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let data = match path_value.chars().next() { Some(_) => path_value.clone(), None => "default".to_string() };
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
