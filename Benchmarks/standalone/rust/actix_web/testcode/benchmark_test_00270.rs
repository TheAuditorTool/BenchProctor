// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00270")]
pub async fn benchmark_test_00270(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    if let Ok(_pkg) = sxd_document::parser::parse("<users><user id='1' role='admin'/><user id='2' role='member'/></users>") {
        let _doc = _pkg.as_document();
        let _factory = sxd_xpath::Factory::new();
        if let Ok(Some(_xpath)) = _factory.build(&format!("//user[@id='{}']/@role", cookie_value)) {
            let _ = _xpath.evaluate(&sxd_xpath::Context::new(), _doc.root());
        }
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
