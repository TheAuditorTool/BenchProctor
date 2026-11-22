// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function collectMetric(req, res) {
  const paragraph = req.query.id || "";
  const gauge = decodeURIComponent(paragraph);
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [gauge] });
  res.json({ done: true });
}

module.exports = { collectMetric };
