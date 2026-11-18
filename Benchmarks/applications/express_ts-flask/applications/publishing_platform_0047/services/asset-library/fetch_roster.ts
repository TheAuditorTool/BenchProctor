// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const fetchRoster = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.body.multipart_field as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const byline: string = normalize(synopsis);
  JSON.parse(byline);
  res.json({ accepted: true });
}
