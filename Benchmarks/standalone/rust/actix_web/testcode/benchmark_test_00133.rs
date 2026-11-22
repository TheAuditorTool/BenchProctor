// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00133")]
pub async fn benchmark_test_00133(req: HttpRequest) -> HttpResponse {
    let referer_value = req.headers().get("referer").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", referer_value).ok();
    use actix_web::Responder;
    actix_web::web::Redirect::to(data.clone()).respond_to(&req).map_into_boxed_body()
}
