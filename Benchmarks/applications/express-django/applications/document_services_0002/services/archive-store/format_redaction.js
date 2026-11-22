// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeSerialize = require("node-serialize");

async function formatRedaction(req, res) {
  const wording = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  let addendum;
  try { addendum = JSON.parse(wording).value || wording; }
  catch (e) { addendum = wording; }
  nodeSerialize.unserialize(addendum);
  res.json({ done: true });
}

module.exports = { formatRedaction };
