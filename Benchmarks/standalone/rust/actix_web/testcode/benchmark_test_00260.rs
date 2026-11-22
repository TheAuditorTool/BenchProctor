// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpRequest, HttpResponse};

#[actix_web::post("/benchmark_test_00260")]
pub async fn benchmark_test_00260(req: HttpRequest) -> HttpResponse {
    let header_value = req.headers().get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match header_value.chars().next() { Some(_) => header_value.clone(), None => "default".to_string() };
    if let Ok((_conn, mut _ldap)) = ldap3::LdapConnAsync::new(&std::env::var("LDAP_URL").unwrap_or_else(|_| "ldap://directory:1389".to_string())).await {
        ldap3::drive!(_conn);
        let _ = _ldap.compare(&format!("uid={},ou=people,dc=example,dc=com", data), "employeeType", "manager").await;
        let _ = _ldap.unbind().await;
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
