// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const reconcileAsset = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.body.multipart_field as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const rendition: string = normalize(notice);
  JSON.parse(rendition);
  res.json({ accepted: true });
}
