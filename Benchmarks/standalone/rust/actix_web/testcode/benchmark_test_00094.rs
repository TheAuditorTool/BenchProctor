// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00094")]
pub async fn benchmark_test_00094(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let captured = user_id.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", data));
}
