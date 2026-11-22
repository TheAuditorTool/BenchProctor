// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function startCheckout(req, res) {
  const wording = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  let backorder;
  try { backorder = JSON.parse(wording).value || wording; }
  catch (e) { backorder = wording; }
  await fetch("http://returns-service:8000/request_return", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: backorder})});
  res.json({ done: true });
}

module.exports = { startCheckout };
