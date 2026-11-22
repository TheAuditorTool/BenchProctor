// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00257() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    let captured = comment_value.clone();
    let reader = move || captured.trim().to_string();
    let data = reader();
    if let Ok((_conn, mut _ldap)) = ldap3::LdapConnAsync::new(&std::env::var("LDAP_URL").unwrap_or_else(|_| "ldap://directory:1389".to_string())).await {
        ldap3::drive!(_conn);
        let _ = _ldap.compare(&format!("uid={},ou=people,dc=example,dc=com", data), "employeeType", "manager").await;
        let _ = _ldap.unbind().await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
