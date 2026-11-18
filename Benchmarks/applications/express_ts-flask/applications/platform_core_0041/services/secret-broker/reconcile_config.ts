// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const reconcileConfig = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.body.multipart_field as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const persona: string = normalize(passage);
  JSON.parse(persona);
  res.json({ accepted: true });
}
