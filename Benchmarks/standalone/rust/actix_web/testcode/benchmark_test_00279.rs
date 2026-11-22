// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00279")]
pub async fn benchmark_test_00279() -> HttpResponse {
    let profile_value = crate::shared::db_fetch_one("SELECT bio FROM profiles LIMIT 1");
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", profile_value).ok();
    let checked_path = format!("/var/app/data/{}", std::path::Path::new(&data).file_name().and_then(|n| n.to_str()).unwrap_or(""));
    tokio::fs::write(&checked_path, "data").await.ok();
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
