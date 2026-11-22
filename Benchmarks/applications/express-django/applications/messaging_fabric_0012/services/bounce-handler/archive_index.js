// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function archiveIndex(req, res) {
  const preface = req.query.id || "";
  const bulletin = decodeURIComponent(preface);
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [bulletin] });
  res.json({ done: true });
}

module.exports = { archiveIndex };
