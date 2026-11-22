// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const vm = require("node:vm");

async function BenchmarkTest00003(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  vm.runInNewContext(String(data), { Math });
  res.json({ done: true });
}

module.exports = { BenchmarkTest00003 };
