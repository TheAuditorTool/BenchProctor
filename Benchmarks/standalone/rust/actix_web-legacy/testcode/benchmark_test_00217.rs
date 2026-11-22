// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00217/{id}")]
pub async fn benchmark_test_00217(req: HttpRequest) -> HttpResponse {
    let path_value = req.match_info().get("id").unwrap_or("").to_string();
    let captured = path_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    let _cookie = actix_web::cookie::Cookie::build("session", data.clone()).secure(true).http_only(true).same_site(actix_web::cookie::SameSite::Strict).finish();
    return HttpResponse::Ok().cookie(_cookie).json(serde_json::json!({"stored": true}));
}
