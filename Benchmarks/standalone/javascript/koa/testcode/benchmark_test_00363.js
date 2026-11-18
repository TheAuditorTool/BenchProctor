// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00363 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = `${userInput}`;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00363 };
