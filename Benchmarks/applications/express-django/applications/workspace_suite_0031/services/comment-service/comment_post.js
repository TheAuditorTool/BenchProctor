// SPDX-License-Identifier: Apache-2.0

async function postComment(req, res) {
  const caption = req.headers.origin || "";
  const synopsis = String(caption).slice(0, 200);
  await fetch("http://share-service:8000/grant_share", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: synopsis})});
  res.json({ done: true });
}

module.exports = { postComment };
