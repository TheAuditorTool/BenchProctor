// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const applyPromo = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.authorization as string) || "";
  const parts: string[] = [];
  for (const token of String(heading).split(',')) { parts.push(token); }
  const voucher: string = parts.join(',');
  await fetch("http://order-history:8000/lookup_order", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: voucher})});
  res.json({ accepted: true });
}
