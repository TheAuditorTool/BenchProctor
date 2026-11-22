// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const renderSummary = async (req: Request, res: Response): Promise<void> => {
  const summary = ((req as any).files?.[0]?.originalname as string) || "";
  const parts: string[] = [];
  for (const token of String(summary).split(',')) { parts.push(token); }
  const consignment: string = parts.join(',');
  net.connect(80, new URL(String(consignment)).hostname);
  res.json({ accepted: true });
}
