// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const crypto = require("crypto");

async function BenchmarkTest00105(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00105 };
