// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeSerialize = require("node-serialize");

async function normalizeRoster(req, res) {
  const paragraph = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  let wording;
  try { wording = JSON.parse(paragraph).value || paragraph; }
  catch (e) { wording = paragraph; }
  nodeSerialize.unserialize(wording);
  res.json({ done: true });
}

module.exports = { normalizeRoster };
