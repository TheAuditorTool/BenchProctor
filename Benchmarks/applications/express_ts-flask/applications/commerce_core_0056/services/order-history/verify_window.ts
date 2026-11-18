// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const verifyWindow = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.body.payload as string) || "";
  const pending: string[] = String(citation).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const backorder: string = collected.join(',');
  http.get(backorder);
  res.json({ accepted: true });
}
