// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function annotatePolicy(req, res) {
  const paragraph = req.query.id || "";
  const persona = decodeURIComponent(paragraph);
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [persona] });
  res.json({ done: true });
}

module.exports = { annotatePolicy };
