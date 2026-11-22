// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00154(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = `${userInput}`;
  const emailMatch = String(data).match(/@([A-Za-z0-9.-]+)$/);
  if (!emailMatch) { res.status(400).json({ error: "not an email address" }); return; }
  const domain = emailMatch[1];
  res.json({ domain }); return;
}

module.exports = { BenchmarkTest00154 };
