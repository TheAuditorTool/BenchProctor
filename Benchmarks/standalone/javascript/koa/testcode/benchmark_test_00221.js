// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const libxmljs = require("libxmljs");

const BenchmarkTest00221 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  await libxmljs.parseXmlAsync(String(userInput), { replaceEntities: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00221 };
