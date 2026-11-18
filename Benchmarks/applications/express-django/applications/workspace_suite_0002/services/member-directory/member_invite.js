// SPDX-License-Identifier: Apache-2.0

async function inviteMember(req, res) {
  const transcript = req.headers.host || "";
  const heading = `${transcript}`;
  await fetch("http://comment-service:8000/post_comment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: heading})});
  res.json({ done: true });
}

module.exports = { inviteMember };
