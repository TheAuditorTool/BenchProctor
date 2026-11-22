// SPDX-License-Identifier: Apache-2.0
use axum::response::IntoResponse;

pub async fn benchmark_test_00081() -> impl IntoResponse {
    let comment_value = crate::shared::db_fetch_one("SELECT text FROM comments LIMIT 1");
    use std::fmt::Write;
    let mut data = String::new();
    write!(&mut data, "{}", comment_value).ok();
    let mut _env = minijinja::Environment::new();
    _env.add_template("profile.html", "<div class=\"profile-bio\">{{ bio }}</div>").ok();
    let _page = _env.get_template("profile.html").and_then(|t| t.render(minijinja::context! { bio => data })).unwrap_or_default();
    return ([("content-type", "text/html")], _page).into_response();
}
