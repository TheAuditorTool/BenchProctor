// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function storeArchive(req, res) {
  const wording = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const addendum = normalize(wording);
  await fetch("http://document-api:8000/upload_document", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
  res.json({ done: true });
}

module.exports = { storeArchive };
