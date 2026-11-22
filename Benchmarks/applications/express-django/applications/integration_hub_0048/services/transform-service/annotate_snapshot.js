// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeSerialize = require("node-serialize");

async function annotateSnapshot(req, res) {
  const citation = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  let handshake;
  try { handshake = JSON.parse(citation).value || citation; }
  catch (e) { handshake = citation; }
  nodeSerialize.unserialize(handshake);
  res.json({ done: true });
}

module.exports = { annotateSnapshot };
