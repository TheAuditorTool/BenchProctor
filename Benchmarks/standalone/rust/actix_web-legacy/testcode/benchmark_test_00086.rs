// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse, web};

#[actix_web::post("/benchmark_test_00086")]
pub async fn benchmark_test_00086(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(referer_value.clone());
    let _chunk = web::Bytes::from(format!("<div>{}</div>", data));
    let mut _response = HttpResponse::Ok();
    _response.content_type("text/html; charset=utf-8");
    return _response.streaming(futures_util::stream::once(async move { Ok::<_, std::convert::Infallible>(_chunk) }));
}
