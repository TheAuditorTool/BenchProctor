// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeSerialize = require("node-serialize");

async function compactHeader(req, res) {
  const memo = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  let ledger;
  try { ledger = JSON.parse(memo).value || memo; }
  catch (e) { ledger = memo; }
  nodeSerialize.unserialize(ledger);
  res.json({ done: true });
}

module.exports = { compactHeader };
