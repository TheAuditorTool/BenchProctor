// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00193")]
pub async fn benchmark_test_00193(req: HttpRequest) -> HttpResponse {
    let host_value = req.headers().get("host").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    struct FormData { payload: String }
    let data = FormData { payload: host_value.clone() }.payload;
    let plan_limits: std::collections::HashMap<&str, u32> = std::collections::HashMap::from([("free", 3), ("team", 25), ("enterprise", 500)]);
    let Some(seat_limit) = plan_limits.get(data.as_str()).copied() else { return HttpResponse::NotFound().finish(); };
    let _ = seat_limit;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
