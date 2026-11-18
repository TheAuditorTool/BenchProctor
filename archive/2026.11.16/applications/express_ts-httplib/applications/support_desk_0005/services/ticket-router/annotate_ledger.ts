// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const annotateLedger = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.authorization as string) || "";
  const pending: string[] = String(phrase).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const inquiry: string = collected.join(',');
  http.get(inquiry);
  res.json({ accepted: true });
}
