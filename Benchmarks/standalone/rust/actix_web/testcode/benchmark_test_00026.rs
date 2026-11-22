// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00026")]
pub async fn benchmark_test_00026(web::Query(query): web::Query<std::collections::HashMap<String, String>>) -> HttpResponse {
    let user_id = query.get("id").cloned().unwrap_or_default();
    let data = user_id.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    let plan_limits: std::collections::HashMap<&str, u32> = std::collections::HashMap::from([("free", 3), ("team", 25), ("enterprise", 500)]);
    let seat_limit = plan_limits.get(data.as_str()).copied().unwrap();
    let _ = seat_limit;
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
