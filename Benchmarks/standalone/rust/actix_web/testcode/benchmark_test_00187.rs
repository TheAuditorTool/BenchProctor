// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00187/{id}")]
pub async fn benchmark_test_00187(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    let data = urlencoding::decode(&path_value).unwrap_or_default().to_string();
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", html_escape::encode_text(&data)));
}
