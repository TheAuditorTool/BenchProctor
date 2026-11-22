// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function exportCheckpoint(req, res) {
  const summary = req.query.id || "";
  const consignment = decodeURIComponent(summary);
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [consignment] });
  res.json({ done: true });
}

module.exports = { exportCheckpoint };
