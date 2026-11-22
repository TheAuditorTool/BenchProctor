// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const storeArchive = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers["x-custom-header"] as string) || "";
  const _raw = phrase;
  const dossier = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://redaction-service:8080/apply_redaction", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: dossier})});
  res.json({ accepted: true });
}
