// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as net from "net";

export const resolveRecord = async (req: Request, res: Response): Promise<void> => {
  const snippet = ((req as any).files?.[0]?.originalname as string) || "";
  const parts: string[] = [];
  for (const token of String(snippet).split(',')) { parts.push(token); }
  const inquiry: string = parts.join(',');
  net.connect(80, new URL(String(inquiry)).hostname);
  res.json({ accepted: true });
}
