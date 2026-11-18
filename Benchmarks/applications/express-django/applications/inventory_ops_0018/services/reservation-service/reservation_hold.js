// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function holdReservation(req, res) {
  const transcript = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const backorder = String(transcript).replace(/\u0000/g, "");
  await fetch("http://catalog-api:8000/lookup_sku", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: backorder})});
  res.json({ done: true });
}

module.exports = { holdReservation };
