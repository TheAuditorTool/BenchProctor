// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00146")]
pub async fn benchmark_test_00146(req: HttpRequest) -> HttpResponse {
    let cookie_value = req.cookie("session_token").map(|c| c.value().to_string()).unwrap_or_default();
    let data = if cookie_value.len() <= 4096 { cookie_value.clone() } else { cookie_value.chars().take(4096).collect() };
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&data) { return HttpResponse::BadRequest().finish(); }
    let processed = data.clone();
    if let Ok((_conn, mut _ldap)) = ldap3::LdapConnAsync::new(&std::env::var("LDAP_URL").unwrap_or_else(|_| "ldap://directory:1389".to_string())).await {
        ldap3::drive!(_conn);
        let _ = _ldap.search("ou=people,dc=example,dc=com", ldap3::Scope::Subtree, &format!("(mail={})", processed), vec!["uid", "cn"]).await;
        let _ = _ldap.unbind().await;
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
