// SPDX-License-Identifier: Apache-2.0

async function storeAttachment(req, res) {
  const blurb = (req.files && req.files[0] && req.files[0].originalname) || "";
  const [inquiry] = String(blurb).split(',');
  await fetch("http://knowledge-index:8000/search_knowledge", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
  res.json({ done: true });
}

module.exports = { storeAttachment };
