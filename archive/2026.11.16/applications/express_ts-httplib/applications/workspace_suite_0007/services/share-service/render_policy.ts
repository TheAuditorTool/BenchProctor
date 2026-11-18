// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const renderPolicy = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.authorization as string) || "";
  const pending: string[] = String(summary).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const subtitle: string = collected.join(',');
  http.get(subtitle);
  res.json({ accepted: true });
}
