// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const verifyConfig = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.multipart_field as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(footnote);
  JSON.parse(handshake);
  res.json({ accepted: true });
}
