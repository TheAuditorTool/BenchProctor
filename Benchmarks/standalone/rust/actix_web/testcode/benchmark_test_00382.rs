// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00382")]
pub async fn benchmark_test_00382(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", user_id).ok();
    let processed = ammonia::clean(&data);
    return HttpResponse::Ok().content_type("text/html").body(format!("<div>{}</div>", processed));
}
