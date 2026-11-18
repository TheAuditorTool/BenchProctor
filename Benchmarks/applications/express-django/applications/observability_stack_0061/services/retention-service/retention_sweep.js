// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function sweepRetention(req, res) {
  const headline = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const trim = (v) => String(v).trim();
  const cohort = trim(headline);
  await fetch("http://dashboard-api:8000/query_dashboard", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
  res.json({ done: true });
}

module.exports = { sweepRetention };
