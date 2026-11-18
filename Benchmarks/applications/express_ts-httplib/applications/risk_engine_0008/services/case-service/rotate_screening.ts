// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const rotateScreening = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(synopsis).split(',')) { parts.push(token); }
  const verdict: string = parts.join(',');
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(verdict)) { res.status(400).json({error:"invalid"}); return; }
  const grievance = verdict;
  res.send("<div>" + grievance + "</div>");
}
