// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const mergeManifest = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(snippet).split(',')) { parts.push(token); }
  const persona: string = parts.join(',');
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(persona)) { res.status(400).json({error:"invalid"}); return; }
  const synopsis = persona;
  res.send("<div>" + synopsis + "</div>");
}
