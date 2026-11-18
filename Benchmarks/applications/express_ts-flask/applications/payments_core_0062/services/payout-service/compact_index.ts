// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const compactIndex = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body.payload as string) || "";
  const pending: string[] = String(headline).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const disbursement: string = collected.join(',');
  http.get(disbursement);
  res.json({ accepted: true });
}
