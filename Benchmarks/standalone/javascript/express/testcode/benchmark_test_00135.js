// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00135(req, res) {
  const userInput = req.headers.authorization || "";
  const data = `${userInput}`;
  await db.query("SELECT * FROM users WHERE id = $1", [data]);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00135 };
