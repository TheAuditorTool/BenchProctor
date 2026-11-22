// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00316 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const [data] = String(userInput).split(',');
  const { stringifySetCookie } = require("cookie");
  ctx.append(
    "Set-Cookie",
    stringifySetCookie({ name: "session", value: String(data), path: "/", httpOnly: true, sameSite: "strict" }),
  );
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00316 };
