// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;

#[actix_web::post("/benchmark_test_00138")]
pub async fn benchmark_test_00138() -> HttpResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let data = comment_value.split([' ', '\t']).filter(|s| !s.is_empty()).collect::<Vec<_>>().join(" ");
    if let Ok(_pkg) = sxd_document::parser::parse("<users><user id='1' role='admin'/><user id='2' role='member'/></users>") {
        let _ = sxd_xpath::evaluate_xpath(&_pkg.as_document(), &format!("count(//user[@role='{}'])", data));
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
