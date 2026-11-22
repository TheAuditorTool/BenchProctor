// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const nodeSerialize = require("node-serialize");

async function formatReceipt(req, res) {
  const subtitle = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  let persona;
  try { persona = JSON.parse(subtitle).value || subtitle; }
  catch (e) { persona = subtitle; }
  nodeSerialize.unserialize(persona);
  res.json({ done: true });
}

module.exports = { formatReceipt };
