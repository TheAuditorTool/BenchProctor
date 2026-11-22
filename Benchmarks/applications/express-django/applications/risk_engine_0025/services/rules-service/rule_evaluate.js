// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function evaluateRule(req, res) {
  const excerpt = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const trim = (v) => String(v).trim();
  const verdict = trim(excerpt);
  await fetch("http://watchlist-sync:8000/sync_watchlist", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: verdict})});
  res.json({ done: true });
}

module.exports = { evaluateRule };
