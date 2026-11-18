// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00315 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(userInput));
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00315 };
