// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00033(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = String(userInput).split(/[ \t]+/).join(" ");
  res.redirect(data);
}

module.exports = { BenchmarkTest00033 };
