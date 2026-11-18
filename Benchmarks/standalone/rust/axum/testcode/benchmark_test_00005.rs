// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;

pub async fn benchmark_test_00005(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let (payload, _origin) = (path_value.clone(), "http");
    let data = payload;
    return ([("content-type", "text/html")], format!("<div>{}</div>", data)).into_response();
}
