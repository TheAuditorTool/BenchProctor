// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00188 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = Buffer.from(userInput, "hex").toString();
  const domain = String(data).match(/@([A-Za-z0-9.-]+)$/)[1];
  ctx.body = { domain }; return;
}

module.exports = { BenchmarkTest00188 };
