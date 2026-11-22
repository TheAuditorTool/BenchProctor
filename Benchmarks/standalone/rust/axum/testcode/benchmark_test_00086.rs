// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;

pub async fn benchmark_test_00086(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let mut data = String::new();
    for token in path_value.split(',') { data = token.to_string(); }
    let _chunk = format!("<div>{}</div>", data);
    return ([("content-type", "text/html; charset=utf-8")], axum::body::Body::from_stream(futures_util::stream::once(async move { Ok::<_, std::convert::Infallible>(_chunk) }))).into_response();
}
