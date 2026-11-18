// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

const BenchmarkTest00281 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00281 };
