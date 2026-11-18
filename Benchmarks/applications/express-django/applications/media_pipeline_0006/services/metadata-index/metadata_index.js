// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function indexMetadata(req, res) {
  const passage = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const montage = passage != null ? passage : '';
  await fetch("http://thumbnail-service:8000/render_thumbnail", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({media_payload: montage})});
  res.json({ done: true });
}

module.exports = { indexMetadata };
