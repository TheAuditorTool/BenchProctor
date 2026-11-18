// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeSerialize = require("node-serialize");

async function BenchmarkTest00041(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = String(userInput).replace(/\u0000/g, "");
  nodeSerialize.unserialize(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00041 };
