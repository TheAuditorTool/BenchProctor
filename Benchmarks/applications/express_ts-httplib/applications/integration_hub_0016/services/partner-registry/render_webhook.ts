// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const renderWebhook = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.headers.host as string) || "";
  const parts: string[] = [];
  for (const token of String(wording).split(',')) { parts.push(token); }
  const handshake: string = parts.join(',');
  net.connect(80, new URL(String(handshake)).hostname);
  res.json({ accepted: true });
}
