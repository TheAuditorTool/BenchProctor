// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function resolveAllocation(req, res) {
  const excerpt = req.query.id || "";
  const restock = decodeURIComponent(excerpt);
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [restock] });
  res.json({ done: true });
}

module.exports = { resolveAllocation };
