// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00219 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  ctx.set("Location", String(data));
  ctx.status = 302;
}

module.exports = { BenchmarkTest00219 };
