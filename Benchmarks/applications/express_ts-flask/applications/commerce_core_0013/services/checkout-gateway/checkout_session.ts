// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const startCheckout = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(wording).split(',')) { parts.push(token); }
  const backorder: string = parts.join(',');
  await fetch("http://returns-service:8000/request_return", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: backorder})});
  res.json({ accepted: true });
}
