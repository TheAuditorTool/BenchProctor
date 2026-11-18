// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function resolveBatch(req, res) {
  const summary = req.query.id || "";
  const bulletin = summary != null ? summary : '';
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [bulletin] });
  res.json({ done: true });
}

module.exports = { resolveBatch };
