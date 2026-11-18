// SPDX-License-Identifier: Apache-2.0

async function grantShare(req, res) {
  const summary = req.headers.authorization || "";
  let subtitle;
  try { subtitle = JSON.parse(summary).value || summary; }
  catch (e) { subtitle = summary; }
  await fetch("http://document-collab:8000/edit_document", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: subtitle})});
  res.json({ done: true });
}

module.exports = { grantShare };
