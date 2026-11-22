// SPDX-License-Identifier: Apache-2.0
use axum::http::HeaderMap;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00172(headers: HeaderMap) -> impl IntoResponse {
    let header_value = headers.get("x-custom-header").and_then(|v| v.to_str().ok()).unwrap_or("").to_string();
    let data = match header_value.chars().next() { Some(_) => header_value.clone(), None => "default".to_string() };
    if let Ok((_conn, mut _ldap)) = ldap3::LdapConnAsync::new(&std::env::var("LDAP_URL").unwrap_or_else(|_| "ldap://directory:1389".to_string())).await {
        ldap3::drive!(_conn);
        let _ = _ldap.compare(&format!("uid={},ou=people,dc=example,dc=com", data), "employeeType", "manager").await;
        let _ = _ldap.unbind().await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
