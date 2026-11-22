// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00119")]
pub async fn benchmark_test_00119(body: web::Bytes) -> HttpResponse {
    let xml_value = String::from_utf8_lossy(&body).to_string();
    static _RE_ENUM: std::sync::LazyLock<regex::Regex> = std::sync::LazyLock::new(|| regex::Regex::new("^(asc|desc|name|created)$").unwrap());
    if !_RE_ENUM.is_match(&xml_value) { return HttpResponse::BadRequest().finish(); }
    let processed = xml_value.clone();
    if let Ok((_conn, mut _ldap)) = ldap3::LdapConnAsync::new(&std::env::var("LDAP_URL").unwrap_or_else(|_| "ldap://directory:1389".to_string())).await {
        ldap3::drive!(_conn);
        let _ = _ldap.search("ou=people,dc=example,dc=com", ldap3::Scope::Subtree, &format!("(mail={})", processed), vec!["uid", "cn"]).await;
        let _ = _ldap.unbind().await;
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
