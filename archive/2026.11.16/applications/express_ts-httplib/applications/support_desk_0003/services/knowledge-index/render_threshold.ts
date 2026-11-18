// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const renderThreshold = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.authorization as string) || "";
  const pending: string[] = String(citation).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const grievance: string = collected.join(',');
  http.get(grievance);
  res.json({ accepted: true });
}
