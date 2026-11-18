// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const saveRevision = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.query.id as string) || "";
  const tokens = String(footnote).split(',').filter((t) => t.length > 0);
  const byline = tokens.join(' ');
  await fetch("http://preview-renderer:8000/render_preview", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
  res.json({ accepted: true });
}
