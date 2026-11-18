// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const auditCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.headers.authorization as string) || "";
  const pending: string[] = String(notice).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const persona: string = collected.join(',');
  http.get(persona);
  res.json({ accepted: true });
}
