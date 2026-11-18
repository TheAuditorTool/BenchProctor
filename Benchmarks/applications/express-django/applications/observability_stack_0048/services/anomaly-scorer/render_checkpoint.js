// SPDX-License-Identifier: Apache-2.0

async function renderCheckpoint(req, res) {
  const excerpt = req.body.field || "";
  const gauge = decodeURIComponent(excerpt);
  res.send("<div>" + gauge + "</div>");
}

module.exports = { renderCheckpoint };
