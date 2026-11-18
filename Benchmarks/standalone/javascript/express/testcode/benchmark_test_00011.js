// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00011(req, res) {
  const userInput = req.body.field || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  await db.query({ name: "user-by-id", text: "SELECT * FROM users WHERE id = $1", values: [data] });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00011 };
