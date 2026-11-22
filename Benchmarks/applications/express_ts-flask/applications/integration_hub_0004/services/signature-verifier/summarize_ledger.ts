// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const summarizeLedger = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(summary).split(',')) { parts.push(token); }
  const handshake: string = parts.join(',');
  res.send("<div>" + handshake + "</div>");
}
