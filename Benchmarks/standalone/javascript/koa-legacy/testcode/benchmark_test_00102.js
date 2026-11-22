// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const vm = require("node:vm");

const BenchmarkTest00102 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = `${userInput}`;
  const _coerced = parseFloat(String(data));
  const parsedNum = _coerced;
  vm.runInNewContext(String(parsedNum), { Math });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00102 };
