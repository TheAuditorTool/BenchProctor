// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function collectCheckpoint(req, res) {
  const notice = req.query.id || "";
  const persona = notice != null ? notice : '';
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [persona] });
  res.json({ done: true });
}

module.exports = { collectCheckpoint };
