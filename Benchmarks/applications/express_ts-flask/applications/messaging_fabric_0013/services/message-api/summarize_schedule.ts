// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const summarizeSchedule = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.multipart_field as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const bulletin: string = normalize(summary);
  JSON.parse(bulletin);
  res.json({ accepted: true });
}
