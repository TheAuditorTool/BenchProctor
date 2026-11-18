// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const configureSample = async (req: Request, res: Response): Promise<void> => {
  const preface = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const transform = (v: string): string => v.trim();
  const cohort: string = transform(preface);
  await fetch("http://retention-service:8000/sweep_retention", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({telemetry_payload: cohort})});
  res.json({ accepted: true });
}
