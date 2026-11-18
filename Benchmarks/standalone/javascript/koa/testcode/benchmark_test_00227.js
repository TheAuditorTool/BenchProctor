// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const libxmljs = require("libxmljs");

const BenchmarkTest00227 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  libxmljs.parseXml(data, { noent: false, dtdload: false, nonet: true });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00227 };
