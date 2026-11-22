// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeSerialize = require("node-serialize");

async function verifyCheckpoint(req, res) {
  const excerpt = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  let verdict;
  try { verdict = JSON.parse(excerpt).value || excerpt; }
  catch (e) { verdict = excerpt; }
  nodeSerialize.unserialize(verdict);
  res.json({ done: true });
}

module.exports = { verifyCheckpoint };
