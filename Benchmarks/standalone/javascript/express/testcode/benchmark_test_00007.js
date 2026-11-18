// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00007(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00007 };
