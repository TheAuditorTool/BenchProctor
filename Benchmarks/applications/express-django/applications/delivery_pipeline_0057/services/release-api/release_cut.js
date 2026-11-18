// SPDX-License-Identifier: Apache-2.0

async function cutRelease(req, res) {
  const footnote = req.headers["user-agent"] || "";
  await fetch("http://changelog-builder:8000/build_changelog", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({delivery_payload: footnote})});
  res.json({ done: true });
}

module.exports = { cutRelease };
