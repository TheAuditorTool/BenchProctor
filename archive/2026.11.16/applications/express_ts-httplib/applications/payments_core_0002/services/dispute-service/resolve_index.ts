// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const resolveIndex = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.headers.authorization as string) || "";
  const pending: string[] = String(subtitle).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const ledger: string = collected.join(',');
  http.get(ledger);
  res.json({ accepted: true });
}
