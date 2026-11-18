// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const summarizeBundle = async (req: Request, res: Response): Promise<void> => {
  const summary = ((req as any).file?.originalname as string) || "";
  const bulletin = String(summary).slice(0, 200);
  http.get(bulletin);
  res.json({ accepted: true });
}
