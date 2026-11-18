// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeSerialize = require("node-serialize");

async function BenchmarkTest00066(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const [data] = String(userInput).split(',');
  nodeSerialize.unserialize(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00066 };
