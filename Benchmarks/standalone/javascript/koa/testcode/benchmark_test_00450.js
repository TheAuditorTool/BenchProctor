// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const libxmljs = require("libxmljs");

const BenchmarkTest00450 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00450 };
