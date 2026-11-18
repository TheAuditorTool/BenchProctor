// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00009")]
pub async fn benchmark_test_00009(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    fn normalize(value: String) -> String { value.trim().to_string() }
    let data = normalize(referer_value.clone());
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", data));
}
