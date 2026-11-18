// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const renderCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(preface).split(',')) { parts.push(token); }
  const remark: string = parts.join(',');
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(remark)) { res.status(400).json({error:"invalid"}); return; }
  const wording = remark;
  res.send("<div>" + wording + "</div>");
}
