// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const libxmljs = require("libxmljs");

const BenchmarkTest00449 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = String(userInput).split(/[ \t]+/).join(" ");
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00449 };
