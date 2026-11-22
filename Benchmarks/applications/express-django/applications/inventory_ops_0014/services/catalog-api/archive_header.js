// SPDX-License-Identifier: Apache-2.0

async function archiveHeader(req, res) {
  const excerpt = req.body.payload || "";
  const restock = `${excerpt}`;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + restock + "</section>"); return;
}

module.exports = { archiveHeader };
