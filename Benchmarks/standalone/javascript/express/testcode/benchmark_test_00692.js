// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00692(req, res) {
  const userInput = req.params.id || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  await db.query("SELECT * FROM users WHERE id = $1", [data]);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00692 };
