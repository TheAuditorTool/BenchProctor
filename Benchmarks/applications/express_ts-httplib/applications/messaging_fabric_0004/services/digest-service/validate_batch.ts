// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const validateBatch = async (req: Request, res: Response): Promise<void> => {
  const paragraph = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(paragraph).split(',')) { parts.push(token); }
  const bulletin: string = parts.join(',');
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(bulletin)) { res.status(400).json({error:"invalid"}); return; }
  const synopsis = bulletin;
  res.send("<div>" + synopsis + "</div>");
}
