// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00713 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  eval(parsedNum);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00713 };
