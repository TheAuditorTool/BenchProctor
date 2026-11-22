// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

const BenchmarkTest00285 = async (ctx) => {
  const userInput = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
  const data = userInput != null ? userInput : '';
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(data)));
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00285 };
