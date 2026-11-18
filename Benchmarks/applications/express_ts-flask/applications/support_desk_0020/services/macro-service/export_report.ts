// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const exportReport = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.body.multipart_field as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const inquiry: string = normalize(phrase);
  JSON.parse(inquiry);
  res.json({ accepted: true });
}
