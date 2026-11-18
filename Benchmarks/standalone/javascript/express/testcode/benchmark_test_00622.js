// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00622(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = String(userInput).replace(/\u0000/g, "");
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00622 };
