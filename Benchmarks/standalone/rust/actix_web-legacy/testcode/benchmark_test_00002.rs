// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00002")]
pub async fn benchmark_test_00002(req: HttpRequest) -> HttpResponse {
    let env_value = std::env::var("APP_SETTING").unwrap_or_default();
    let (payload, _origin) = (env_value.clone(), "http");
    let data = payload;
    use actix_web::Responder;
    actix_web::web::Redirect::to(data.clone()).respond_to(&req).map_into_boxed_body()
}
