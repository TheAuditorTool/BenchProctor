// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const buildStatement = async (req: Request, res: Response): Promise<void> => {
  const headline = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const parts: string[] = [];
  for (const token of String(headline).split(',')) { parts.push(token); }
  const remittance: string = parts.join(',');
  await fetch("http://refund-service:8080/issue_refund", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: remittance})});
  res.json({ accepted: true });
}
