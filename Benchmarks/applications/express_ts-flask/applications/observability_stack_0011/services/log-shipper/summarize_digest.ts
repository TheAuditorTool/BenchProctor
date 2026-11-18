// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const summarizeDigest = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body.field as string) || "";
  const gauge = String(caption).slice(0, 200);
  JSON.parse(gauge);
  res.json({ accepted: true });
}
