// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const stream = require("node:stream");

const BenchmarkTest00202 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  ctx.type = "html";
  ctx.body = stream.Readable.from(["<section>" + data + "</section>"]);
}

module.exports = { BenchmarkTest00202 };
