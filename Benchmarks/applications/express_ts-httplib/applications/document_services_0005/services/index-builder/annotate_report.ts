// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const annotateReport = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.host as string) || "";
  const parts: string[] = [];
  for (const token of String(footnote).split(',')) { parts.push(token); }
  const addendum: string = parts.join(',');
  net.connect(80, new URL(String(addendum)).hostname);
  res.json({ accepted: true });
}
