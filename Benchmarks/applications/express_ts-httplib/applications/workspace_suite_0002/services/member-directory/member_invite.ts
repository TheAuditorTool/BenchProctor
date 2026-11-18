// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const inviteMember = async (req: Request, res: Response): Promise<void> => {
  const transcript = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const heading = String(transcript).replace(/\u0000/g, "");
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://comment-service:8080/post_comment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: heading})});
  res.json({ accepted: true });
}
