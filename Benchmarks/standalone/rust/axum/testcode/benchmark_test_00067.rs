// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;
use axum::response::Json;

pub async fn benchmark_test_00067(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let data = path_value.to_string();
    if let Ok((_conn, mut _ldap)) = ldap3::LdapConnAsync::new(&std::env::var("LDAP_URL").unwrap_or_else(|_| "ldap://directory:1389".to_string())).await {
        ldap3::drive!(_conn);
        let _ = _ldap.search("ou=people,dc=example,dc=com", ldap3::Scope::Subtree, &format!("(mail={})", data), vec!["uid", "cn"]).await;
        let _ = _ldap.unbind().await;
    }
    Json(serde_json::json!({"count": 0})).into_response()
}
