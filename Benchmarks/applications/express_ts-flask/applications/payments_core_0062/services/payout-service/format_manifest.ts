// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const formatManifest = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body.field as string) || "";
  const disbursement = String(headline).slice(0, 200);
  JSON.parse(disbursement);
  res.json({ accepted: true });
}
