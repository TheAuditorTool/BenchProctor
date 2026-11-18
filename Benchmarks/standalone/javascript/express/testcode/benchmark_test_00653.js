// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const crypto = require("crypto");

async function BenchmarkTest00653(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00653 };
