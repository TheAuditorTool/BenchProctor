// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse, web};

#[actix_web::post("/benchmark_test_00230")]
pub async fn benchmark_test_00230(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(header_value.clone());
    let _chunk = web::Bytes::from(format!("<div>{}</div>", data));
    let mut _response = HttpResponse::Ok();
    _response.content_type("text/html; charset=utf-8");
    return _response.streaming(futures_util::stream::once(async move { Ok::<_, std::convert::Infallible>(_chunk) }));
}
