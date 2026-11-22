// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00083(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const [data] = String(userInput).split(',');
  const { stringifySetCookie } = require("cookie");
  res.append(
    "Set-Cookie",
    stringifySetCookie({ name: "session", value: String(data), path: "/", httpOnly: true, sameSite: "strict" }),
  );
  res.json({ done: true });
}

module.exports = { BenchmarkTest00083 };
