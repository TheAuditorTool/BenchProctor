// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeSerialize = require("node-serialize");

async function archiveReceipt(req, res) {
  const note = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  let cohort;
  try { cohort = JSON.parse(note).value || note; }
  catch (e) { cohort = note; }
  nodeSerialize.unserialize(cohort);
  res.json({ done: true });
}

module.exports = { archiveReceipt };
