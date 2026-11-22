// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as nodeUtil from "util";

export const queueFulfillment = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.headers["x-custom-header"] as string) || "";
  const voucher = nodeUtil.format("%s", subject);
  await fetch("http://promo-service:8000/apply_promo", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: voucher})});
  res.json({ accepted: true });
}
