// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function archiveSummary(req, res) {
  const preface = req.query.id || "";
  const cohort = preface != null ? preface : '';
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [cohort] });
  res.json({ done: true });
}

module.exports = { archiveSummary };
