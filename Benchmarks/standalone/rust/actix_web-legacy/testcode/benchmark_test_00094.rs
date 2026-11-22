// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse, web};

#[actix_web::post("/benchmark_test_00094/{id}")]
pub async fn benchmark_test_00094(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    let captured = path_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let processed = html_escape::encode_text(&data).to_string();
    let _chunk = web::Bytes::from(format!("<div>{}</div>", processed));
    let mut _response = HttpResponse::Ok();
    _response.content_type("text/html; charset=utf-8");
    return _response.streaming(futures_util::stream::once(async move { Ok::<_, std::convert::Infallible>(_chunk) }));
}
