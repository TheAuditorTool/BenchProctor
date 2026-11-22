// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse, web};

#[actix_web::post("/benchmark_test_00241")]
pub async fn benchmark_test_00241(req: HttpRequest, web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    struct FormData { payload: String }
    let data = FormData { payload: user_id.clone() }.payload;
    use actix_web::Responder;
    actix_web::web::Redirect::to(data.clone()).respond_to(&req).map_into_boxed_body()
}
