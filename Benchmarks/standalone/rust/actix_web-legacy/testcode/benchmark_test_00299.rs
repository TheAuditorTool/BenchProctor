// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00299")]
pub async fn benchmark_test_00299(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = header_value.replace("\t", " ");
    let _coerced = data.parse::<f64>().unwrap_or(0.0);
    let processed = _coerced.to_string();
    if let Ok(_pkg) = sxd_document::parser::parse("<users><user id='1' role='admin'/><user id='2' role='member'/></users>") {
        let _doc = _pkg.as_document();
        let _factory = sxd_xpath::Factory::new();
        if let Ok(Some(_xpath)) = _factory.build(&format!("//user[@id='{}']/@role", processed)) {
            let _ = _xpath.evaluate(&sxd_xpath::Context::new(), _doc.root());
        }
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
