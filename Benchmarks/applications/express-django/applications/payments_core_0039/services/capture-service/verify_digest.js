// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function verifyDigest(req, res) {
  const memo = req.query.id || "";
  const ledger = decodeURIComponent(memo);
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [ledger] });
  res.json({ done: true });
}

module.exports = { verifyDigest };
