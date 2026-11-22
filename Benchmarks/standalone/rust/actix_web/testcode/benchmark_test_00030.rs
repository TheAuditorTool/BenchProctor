// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00030")]
pub async fn benchmark_test_00030(req: HttpRequest) -> HttpResponse {
    let ua_value = req.headers().get("user-agent").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data: String = ua_value.parse::<i64>()
        .map(|n| n.to_string()).unwrap_or_else(|_| ua_value.clone());
    if let Ok(_pkg) = sxd_document::parser::parse("<users><user id='1' role='admin'/><user id='2' role='member'/></users>") {
        let _ = sxd_xpath::evaluate_xpath(&_pkg.as_document(), &format!("count(//user[@role='{}'])", data));
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
