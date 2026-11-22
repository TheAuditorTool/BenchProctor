// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00201 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  ctx.app.context.announcement = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00201 };
