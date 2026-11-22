// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00037")]
pub async fn benchmark_test_00037(body: web::Bytes) -> HttpResponse {
    let json_value = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("payload").and_then(|p| p.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let data = json_value.to_string();
    static _RE_INPUT: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^[a-zA-Z0-9 _.%~\\-]+$").unwrap());
    if !_RE_INPUT.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    if let Ok(_pkg) = sxd_document::parser::parse("<users><user id='1' role='admin'/><user id='2' role='member'/></users>") {
        let _doc = _pkg.as_document();
        let _factory = sxd_xpath::Factory::new();
        if let Ok(Some(_xpath)) = _factory.build(&format!("//user[@id='{}']/@role", processed)) {
            let _ = _xpath.evaluate(&sxd_xpath::Context::new(), _doc.root());
        }
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
