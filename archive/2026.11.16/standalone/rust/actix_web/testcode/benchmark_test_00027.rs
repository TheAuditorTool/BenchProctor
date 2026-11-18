// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00027")]
pub async fn benchmark_test_00027(req: HttpRequest) -> HttpResponse {
    let auth_header = req.headers().get("authorization").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = auth_header.to_string();
    let processed = html_escape::encode_text(&data).to_string();
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", processed));
}
