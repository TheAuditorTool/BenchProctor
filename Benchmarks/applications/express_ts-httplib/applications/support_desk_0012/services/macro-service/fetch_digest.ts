// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const fetchDigest = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(summary).split(',')) { parts.push(token); }
  const grievance: string = parts.join(',');
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(grievance)) { res.status(400).json({error:"invalid"}); return; }
  const inquiry = grievance;
  res.send("<div>" + inquiry + "</div>");
}
