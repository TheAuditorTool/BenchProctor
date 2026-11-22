// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const mintToken = async (req: Request, res: Response): Promise<void> => {
  const tagline = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(tagline).split(',')) { parts.push(token); }
  const persona: string = parts.join(',');
  await fetch("http://session-store:8000/create_session", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
  res.json({ accepted: true });
}
