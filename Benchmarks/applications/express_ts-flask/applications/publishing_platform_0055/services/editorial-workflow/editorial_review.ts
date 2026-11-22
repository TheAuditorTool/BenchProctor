// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const reviewEditorial = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(synopsis).split(',')) { parts.push(token); }
  const byline: string = parts.join(',');
  await fetch("http://preview-renderer:8000/render_preview", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: byline})});
  res.json({ accepted: true });
}
