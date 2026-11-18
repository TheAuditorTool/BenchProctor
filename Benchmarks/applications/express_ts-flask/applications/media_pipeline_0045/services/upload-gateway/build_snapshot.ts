// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const buildSnapshot = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.body.payload as string) || "";
  const pending: string[] = String(notice).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const rendition: string = collected.join(',');
  http.get(rendition);
  res.json({ accepted: true });
}
