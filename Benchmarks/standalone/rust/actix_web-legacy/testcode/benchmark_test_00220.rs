// SPDX-License-Identifier: Apache-2.0
use actix_web::{HttpResponse, web};

#[actix_web::post("/benchmark_test_00220")]
pub async fn benchmark_test_00220(body: web::Bytes) -> HttpResponse {
    let graphql_var = serde_json::from_slice::<serde_json::Value>(&body).ok().and_then(|v| v.get("variables").and_then(|vs| vs.get("input")).and_then(|i| i.as_str()).map(|s| s.to_string())).unwrap_or_default();
    let _prefix: String = graphql_var.chars().next().map(|c| c.to_lowercase().to_string()).unwrap_or_default();
    let data = match _prefix.as_str() {
        "h" => graphql_var.to_lowercase(),
        "f" => graphql_var.to_uppercase(),
        _ => graphql_var.trim().to_string(),
    };
    if let Ok((_conn, mut _ldap)) = ldap3::LdapConnAsync::new(&std::env::var("LDAP_URL").unwrap_or_else(|_| "ldap://directory:1389".to_string())).await {
        ldap3::drive!(_conn);
        let _ = _ldap.compare(&format!("uid={},ou=people,dc=example,dc=com", data), "employeeType", "manager").await;
        let _ = _ldap.unbind().await;
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
