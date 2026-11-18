// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const shipLog = async (req: Request, res: Response): Promise<void> => {
  const caption = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const gauge = String(caption).replace(/\u0000/g, "");
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://metrics-ingest:8000/ingest_metric", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: gauge})});
  res.json({ accepted: true });
}
