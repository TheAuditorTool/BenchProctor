// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeUtil = require("util");
const stream = require("node:stream");

const BenchmarkTest00202 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = nodeUtil.format("%s", userInput);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  ctx.type = "html";
  ctx.body = stream.Readable.from(["<section>" + processed + "</section>"]);
}

module.exports = { BenchmarkTest00202 };
