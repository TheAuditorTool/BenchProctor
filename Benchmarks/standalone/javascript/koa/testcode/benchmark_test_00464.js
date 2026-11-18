// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00464 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
  if (!row) { ctx.status = 404; ctx.body = {error:"not found"}; return; }
  const value = row.name;
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00464 };
