// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const exportDigest = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body.multipart_field as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const gauge: string = normalize(caption);
  JSON.parse(gauge);
  res.json({ accepted: true });
}
