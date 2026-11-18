// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function renderWaybill(req, res) {
  const footnote = req.query.id || "";
  const parcel = footnote != null ? footnote : '';
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [parcel] });
  res.json({ done: true });
}

module.exports = { renderWaybill };
