// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildStatement = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const remittance: string = transform(headline);
  await fetch("http://refund-service:8000/issue_refund", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: remittance})});
  res.json({ accepted: true });
}
