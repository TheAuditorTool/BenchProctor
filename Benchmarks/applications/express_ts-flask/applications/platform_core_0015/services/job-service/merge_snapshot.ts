// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const mergeSnapshot = async (req: Request, res: Response): Promise<void> => {
  const note = (req.body.multipart_field as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(note);
  JSON.parse(handshake);
  res.json({ accepted: true });
}
