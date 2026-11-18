// SPDX-License-Identifier: Apache-2.0

async function postComment(req, res) {
  const remark = (req.file && req.file.originalname) || "";
  const [synopsis] = String(remark).split(',');
  await fetch("http://presence-hub:8000/track_presence", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: synopsis})});
  res.json({ done: true });
}

module.exports = { postComment };
