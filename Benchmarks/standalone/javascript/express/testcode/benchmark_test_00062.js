// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00062(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const domain = String(data).match(/@([A-Za-z0-9.-]+)$/)[1];
  res.json({ domain }); return;
}

module.exports = { BenchmarkTest00062 };
