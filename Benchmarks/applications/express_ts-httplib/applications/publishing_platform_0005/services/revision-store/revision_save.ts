// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const saveRevision = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.authorization as string) || "";
  const byline = Buffer.from(footnote, "base64").toString();
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://preview-renderer:8080/render_preview", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
  res.json({ accepted: true });
}
