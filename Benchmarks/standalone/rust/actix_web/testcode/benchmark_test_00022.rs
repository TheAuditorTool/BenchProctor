// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00022")]
pub async fn benchmark_test_00022() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(db_value.clone());
    let processed = html_escape::encode_text(&data).to_string();
    let _chunk = web::Bytes::from(format!("<div>{}</div>", processed));
    let mut _response = HttpResponse::Ok();
    _response.content_type("text/html; charset=utf-8");
    return _response.streaming(futures_util::stream::once(async move { Ok::<_, std::convert::Infallible>(_chunk) }));
}
