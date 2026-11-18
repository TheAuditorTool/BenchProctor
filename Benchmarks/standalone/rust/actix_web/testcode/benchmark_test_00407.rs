// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00407/{id}")]
pub async fn benchmark_test_00407(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", path_value).ok();
    crate::shared::set_cookie(&format!("session={}; HttpOnly; SameSite=Strict", data));
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
