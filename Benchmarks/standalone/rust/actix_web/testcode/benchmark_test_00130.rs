// SPDX-License-Identifier: Apache-2.0
use actix_web::HttpResponse;
use futures_util::StreamExt;

#[actix_web::post("/benchmark_test_00130")]
pub async fn benchmark_test_00130(mut payload: actix_multipart::Multipart) -> HttpResponse {
    let multipart_value = {
        let mut _mv = String::new();
        if let Some(Ok(mut _field)) = payload.next().await {
            let mut _buf: Vec<u8> = Vec::new();
            while let Some(Ok(_chunk)) = _field.next().await {
                _buf.extend_from_slice(&_chunk);
            }
            _mv = String::from_utf8_lossy(&_buf).to_string();
        }
        _mv
    };
    let (payload, _origin) = (multipart_value.clone(), "http");
    let data = payload;
    if let Ok((_conn, mut _ldap)) = ldap3::LdapConnAsync::new(&std::env::var("LDAP_URL").unwrap_or_else(|_| "ldap://directory:1389".to_string())).await {
        ldap3::drive!(_conn);
        let _ = _ldap.search("ou=people,dc=example,dc=com", ldap3::Scope::Subtree, &format!("(mail={})", data), vec!["uid", "cn"]).await;
        let _ = _ldap.unbind().await;
    }
    HttpResponse::Ok().json(serde_json::json!({"stored": true}))
}
