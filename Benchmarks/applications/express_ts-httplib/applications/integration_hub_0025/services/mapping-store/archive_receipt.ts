// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const archiveReceipt = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.authorization as string) || "";
  const parts: string[] = [];
  for (const token of String(footnote).split(',')) { parts.push(token); }
  const handshake: string = parts.join(',');
  if (!/^(asc|desc|name|created)$/.test(String(handshake))) { res.status(400).json({error:"invalid"}); return; }
  const blurb = handshake;
  res.send("<div>" + blurb + "</div>");
}
