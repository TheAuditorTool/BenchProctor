// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const grantShare = async (req: Request, res: Response): Promise<void> => {
  const summary = fs.readFileSync("/tmp/data", "utf8");
  let subtitle;
  try { subtitle = JSON.parse(summary).value || ""; }
  catch (e) { subtitle = String(summary); }
  await fetch("http://document-collab:8080/edit_document", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: subtitle})});
  res.json({ accepted: true });
}
