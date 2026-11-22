// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const renderRoster = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.headers.host as string) || "";
  const parts: string[] = [];
  for (const token of String(transcript).split(',')) { parts.push(token); }
  const consignment: string = parts.join(',');
  net.connect(80, new URL(String(consignment)).hostname);
  res.json({ accepted: true });
}
