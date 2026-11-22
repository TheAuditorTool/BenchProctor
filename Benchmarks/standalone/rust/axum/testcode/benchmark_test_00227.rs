// SPDX-License-Identifier: Apache-2.0
use axum::extract::Path;
use axum::response::IntoResponse;

pub async fn benchmark_test_00227(Path(path_id): Path<String>) -> impl IntoResponse {
    let path_value = path_id.clone();
    let transform = |v: String| v.trim().to_string();
    let data = transform(path_value.clone());
    let processed = ammonia::clean(&data);
    let mut _env = minijinja::Environment::new();
    _env.add_template("profile.html", "<div class=\"profile-bio\">{{ bio|safe }}</div>").ok();
    let _page = _env.get_template("profile.html").and_then(|t| t.render(minijinja::context! { bio => processed })).unwrap_or_default();
    return ([("content-type", "text/html")], _page).into_response();
}
