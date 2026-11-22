// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00304 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const { serialize } = require("cookie");
  ctx.append(
    "Set-Cookie",
    serialize("session", String(data), { path: "/", httpOnly: true, sameSite: "strict", secure: true }),
  );
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00304 };
