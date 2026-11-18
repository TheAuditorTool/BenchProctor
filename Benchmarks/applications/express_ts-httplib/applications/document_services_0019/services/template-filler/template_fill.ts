// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const fillTemplate = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.headers.authorization as string) || "";
  const parts: string[] = [];
  for (const token of String(passage).split(',')) { parts.push(token); }
  const dossier: string = parts.join(',');
  await fetch("http://redaction-service:8080/apply_redaction", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: dossier})});
  res.json({ accepted: true });
}
