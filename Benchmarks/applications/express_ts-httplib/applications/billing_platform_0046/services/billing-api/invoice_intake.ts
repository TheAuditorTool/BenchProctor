// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const submitInvoice = async (req: Request, res: Response): Promise<void> => {
  const remark = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(remark);
  const remittance: string = readInput();
  await fetch("http://settlement-service:8080/run_settlement", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: remittance})});
  res.json({ accepted: true });
}
