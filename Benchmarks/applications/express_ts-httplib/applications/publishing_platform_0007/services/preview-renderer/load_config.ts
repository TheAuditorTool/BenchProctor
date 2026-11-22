// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const loadConfig = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers.host as string) || "";
  const parts: string[] = [];
  for (const token of String(remark).split(',')) { parts.push(token); }
  const byline: string = parts.join(',');
  net.connect(80, new URL(String(byline)).hostname);
  res.json({ accepted: true });
}
