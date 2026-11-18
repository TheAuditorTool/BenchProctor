// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const auditCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const notice = ((req as any).file?.originalname as string) || "";
  const persona = String(notice).slice(0, 200);
  http.get(persona);
  res.json({ accepted: true });
}
