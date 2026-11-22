// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const libxmljs = require("libxmljs");

const BenchmarkTest00223 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  await libxmljs.parseXmlAsync(String(data), { replaceEntities: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00223 };
