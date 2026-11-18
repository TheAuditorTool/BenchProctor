// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function annotateSnapshot(req, res) {
  const subject = req.query.id || "";
  const parcel = subject != null ? subject : '';
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [parcel] });
  res.json({ done: true });
}

module.exports = { annotateSnapshot };
