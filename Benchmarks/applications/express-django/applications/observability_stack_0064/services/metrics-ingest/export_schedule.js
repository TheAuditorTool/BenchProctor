// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function exportSchedule(req, res) {
  const tagline = req.query.id || "";
  const gauge = decodeURIComponent(tagline);
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [gauge] });
  res.json({ done: true });
}

module.exports = { exportSchedule };
