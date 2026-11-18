// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00580(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = String(userInput).split(/[ \t]+/).join(" ");
  res.cookie("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00580 };
