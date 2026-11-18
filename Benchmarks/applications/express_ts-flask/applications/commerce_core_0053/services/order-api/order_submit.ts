// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const placeOrder = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.query.id as string) || "";
  const _raw = memo;
  const voucher = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://cart-service:8000/update_cart", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: voucher})});
  res.json({ accepted: true });
}
