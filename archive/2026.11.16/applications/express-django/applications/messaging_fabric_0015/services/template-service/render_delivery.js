// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function renderDelivery(req, res) {
  const heading = req.query.id || "";
  const bulletin = heading != null ? heading : '';
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [bulletin] });
  res.json({ done: true });
}

module.exports = { renderDelivery };
