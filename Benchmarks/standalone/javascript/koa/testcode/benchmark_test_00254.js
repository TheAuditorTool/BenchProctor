// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const path = require("path");
const fs = require("fs");

const BenchmarkTest00254 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = userInput != null ? userInput : '';
  const resolved = path.resolve("/var/app/data", data);
  if (!resolved.startsWith("/var/app/data/")) { ctx.status = 403; ctx.body = {error:"forbidden"}; return; }
  const checkedPath = resolved;
  fs.unlinkSync(checkedPath);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00254 };
