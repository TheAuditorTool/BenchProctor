// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00282")]
pub async fn benchmark_test_00282(req: HttpRequest) -> HttpResponse {
    let forwarded_ip = req.headers().get("x-forwarded-for").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let transform = |v: String| v.trim().to_string();
    let data = transform(forwarded_ip.clone());
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&data) { return HttpResponse::BadRequest().finish(); }
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
