// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const queueFulfillment = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.body.payload as string) || "";
  const voucher = `${subject}`;
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://promo-service:8080/apply_promo", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: voucher})});
  res.json({ accepted: true });
}
