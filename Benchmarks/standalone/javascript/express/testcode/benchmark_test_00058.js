// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const xpath = require("xpath");
const xmldom = require("@xmldom/xmldom");

async function BenchmarkTest00058(req, res) {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
  xpath.select("//user[name='" + data + "']", xmlDoc);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00058 };
