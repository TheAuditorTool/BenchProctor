// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const renderProfile = async (req: Request, res: Response): Promise<void> => {
  const footnote = ((req as any).file?.originalname as string) || "";
  const parcel = String(footnote).slice(0, 200);
  http.get(parcel);
  res.json({ accepted: true });
}
