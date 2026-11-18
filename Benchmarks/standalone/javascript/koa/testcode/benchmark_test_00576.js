// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeSerialize = require("node-serialize");

const BenchmarkTest00576 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const [data] = String(userInput).split(',');
  nodeSerialize.unserialize(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00576 };
