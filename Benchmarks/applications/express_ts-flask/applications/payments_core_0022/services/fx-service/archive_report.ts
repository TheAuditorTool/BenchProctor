// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const archiveReport = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.body.field as string) || "";
  const ledger = String(subject).slice(0, 200);
  JSON.parse(ledger);
  res.json({ accepted: true });
}
