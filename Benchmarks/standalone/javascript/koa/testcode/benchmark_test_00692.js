// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00692 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = Buffer.from(userInput, "hex").toString();
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00692 };
