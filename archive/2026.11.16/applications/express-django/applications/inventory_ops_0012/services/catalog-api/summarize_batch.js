// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function summarizeBatch(req, res) {
  const phrase = req.query.id || "";
  const backorder = phrase != null ? phrase : '';
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [backorder] });
  res.json({ done: true });
}

module.exports = { summarizeBatch };
