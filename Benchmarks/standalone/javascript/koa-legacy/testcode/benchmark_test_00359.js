// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const crypto = require("crypto");

const BenchmarkTest00359 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const digest = await crypto.subtle.digest("SHA-256", Buffer.from(String(data)));
  ctx.body = { fingerprint: Buffer.from(digest).toString("hex") }; return;
}

module.exports = { BenchmarkTest00359 };
