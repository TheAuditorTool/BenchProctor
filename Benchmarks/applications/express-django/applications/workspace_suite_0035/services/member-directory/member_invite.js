// SPDX-License-Identifier: Apache-2.0

async function inviteMember(req, res) {
  const paragraph = req.body.payload || "";
  let wording;
  try { wording = JSON.parse(paragraph).value || ""; }
  catch (e) { wording = String(paragraph); }
  await fetch("http://activity-feed:8000/stream_activity", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: wording})});
  res.json({ done: true });
}

module.exports = { inviteMember };
