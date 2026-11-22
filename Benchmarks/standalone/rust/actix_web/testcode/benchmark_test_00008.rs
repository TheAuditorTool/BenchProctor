// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00008")]
pub async fn benchmark_test_00008() -> HttpResponse {
    let db_value = crate::shared::db_fetch_one("SELECT name FROM users LIMIT 1");
    let _prefix: String = db_value.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => db_value.to_lowercase(),
        "f" => db_value.to_uppercase(),
        _ => db_value.trim().to_string(),
    };
    let plan_limits: std::collections::HashMap<&str, u32> = std::collections::HashMap::from([("free", 3), ("team", 25), ("enterprise", 500)]);
    let seat_limit = plan_limits.get(data.as_str()).copied().unwrap();
    let _ = seat_limit;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
