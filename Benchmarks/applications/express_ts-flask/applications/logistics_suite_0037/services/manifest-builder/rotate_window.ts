// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const rotateWindow = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.payload as string) || "";
  const pending: string[] = String(footnote).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const consignment: string = collected.join(',');
  http.get(consignment);
  res.json({ accepted: true });
}
