// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const compactSchedule = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.host as string) || "";
  const parts: string[] = [];
  for (const token of String(citation).split(',')) { parts.push(token); }
  const parcel: string = parts.join(',');
  net.connect(80, new URL(String(parcel)).hostname);
  res.json({ accepted: true });
}
