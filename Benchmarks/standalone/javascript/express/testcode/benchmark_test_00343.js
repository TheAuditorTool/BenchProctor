// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const crypto = require("crypto");
const nodeUtil = require("util");

async function BenchmarkTest00343(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = nodeUtil.format("%s", userInput);
  crypto.createCipheriv("des-ede3-ecb", Buffer.alloc(24), null).update(String(data));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00343 };
