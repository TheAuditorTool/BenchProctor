// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const applyMacro = async (req: Request, res: Response): Promise<void> => {
  const summary = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = summary;
  const grievance = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://escalation-service:8080/raise_escalation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
  res.json({ accepted: true });
}
