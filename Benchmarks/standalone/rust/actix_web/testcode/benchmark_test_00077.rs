// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00077")]
pub async fn benchmark_test_00077(req: HttpRequest) -> HttpResponse {
    let forwarded_ip = req.headers().get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", forwarded_ip).ok();
    let plan_limits: std::collections::HashMap<&str, u32> = std::collections::HashMap::from([("free", 3), ("team", 25), ("enterprise", 500)]);
    let Some(seat_limit) = plan_limits.get(data.as_str()).copied() else { return HttpResponse::NotFound().finish(); };
    let _ = seat_limit;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
