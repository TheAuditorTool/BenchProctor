// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const publishCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(citation).split(',')) { parts.push(token); }
  const backorder: string = parts.join(',');
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(backorder)) { res.status(400).json({error:"invalid"}); return; }
  const restock = backorder;
  res.send("<div>" + restock + "</div>");
}
