// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const libxmljs = require("libxmljs");

const BenchmarkTest00332 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00332 };
