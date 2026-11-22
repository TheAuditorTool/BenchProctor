// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { createClient } from "redis";

export const placeOrder = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const headline = (await _cache.get("user_data")) || "";
  const parts: string[] = [];
  for (const token of String(headline).split(',')) { parts.push(token); }
  const backorder: string = parts.join(',');
  await fetch("http://cart-service:8080/update_cart", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: backorder})});
  res.json({ accepted: true });
}
