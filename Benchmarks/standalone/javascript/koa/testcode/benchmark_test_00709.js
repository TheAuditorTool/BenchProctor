// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeUtil = require("util");

const BenchmarkTest00709 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = nodeUtil.format("%s", userInput);
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  ctx.body = { token };
}

module.exports = { BenchmarkTest00709 };
