// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse, web};

#[actix_web::post("/benchmark_test_00118")]
pub async fn benchmark_test_00118(req: HttpRequest, web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let data = match user_id.chars().next() { Some(_) => user_id.clone(), None => "default".to_string() };
    use actix_web::Responder;
    actix_web::web::Redirect::to(data.clone()).respond_to(&req).map_into_boxed_body()
}
