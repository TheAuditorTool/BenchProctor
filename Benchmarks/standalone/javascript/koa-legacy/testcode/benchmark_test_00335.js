// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const stream = require("node:stream");

const BenchmarkTest00335 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = `${userInput}`;
  ctx.type = "html";
  ctx.body = stream.Readable.from(["<section>" + data + "</section>"]);
}

module.exports = { BenchmarkTest00335 };
