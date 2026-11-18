// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const recordConsent = async (req: Request, res: Response): Promise<void> => {
  const phrase = ((req as any).file?.originalname as string) || "";
  const _raw = phrase;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://directory-sync:8080/sync_directory", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
  res.json({ accepted: true });
}
