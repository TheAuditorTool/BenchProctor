// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;

pub async fn benchmark_test_00093() -> impl IntoResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(db_value.clone());
    let processed = html_escape::encode_text(&data).to_string();
    let _chunk = format!("<div>{}</div>", processed);
    return ([("content-type", "text/html; charset=utf-8")], axum::body::Body::from_stream(futures_util::stream::once(async move { Ok::<_, std::convert::Infallible>(_chunk) }))).into_response();
}
