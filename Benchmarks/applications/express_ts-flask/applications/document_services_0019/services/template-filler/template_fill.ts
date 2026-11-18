// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const fillTemplate = async (req: Request, res: Response): Promise<void> => {
  const passage = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(passage);
  const dossier: string = readInput();
  await fetch("http://redaction-service:8000/apply_redaction", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: dossier})});
  res.json({ accepted: true });
}
