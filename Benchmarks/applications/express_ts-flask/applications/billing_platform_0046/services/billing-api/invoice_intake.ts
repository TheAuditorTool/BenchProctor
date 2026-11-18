// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const submitInvoice = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(remark).split(',')) { parts.push(token); }
  const remittance: string = parts.join(',');
  await fetch("http://settlement-service:8000/run_settlement", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: remittance})});
  res.json({ accepted: true });
}
