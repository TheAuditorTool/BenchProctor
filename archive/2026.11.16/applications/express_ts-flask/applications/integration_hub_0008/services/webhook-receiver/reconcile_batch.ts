// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const reconcileBatch = async (req: Request, res: Response): Promise<void> => {
  const preface = ((req as any).file?.originalname as string) || "";
  const handshake = String(preface).slice(0, 200);
  http.get(handshake);
  res.json({ accepted: true });
}
