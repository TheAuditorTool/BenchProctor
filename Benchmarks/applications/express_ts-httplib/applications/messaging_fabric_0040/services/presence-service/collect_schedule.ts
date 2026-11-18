// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const collectSchedule = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(preface).split(',')) { parts.push(token); }
  const bulletin: string = parts.join(',');
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(bulletin)) { res.status(400).json({error:"invalid"}); return; }
  const notice = bulletin;
  res.send("<div>" + notice + "</div>");
}
