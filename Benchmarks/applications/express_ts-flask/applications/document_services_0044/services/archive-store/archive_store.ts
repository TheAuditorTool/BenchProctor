// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const storeArchive = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.body?.multipart_field as string) || "";
  const tokens = String(phrase).split(',').filter((t) => t.length > 0);
  const dossier = tokens.join(' ');
  await fetch("http://redaction-service:8000/apply_redaction", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: dossier})});
  res.json({ accepted: true });
}
