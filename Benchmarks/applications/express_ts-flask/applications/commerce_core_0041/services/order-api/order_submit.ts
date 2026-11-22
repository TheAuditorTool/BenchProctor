// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const placeOrder = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.headers.host as string) || "";
  const transform = (v: string): string => v.trim();
  const backorder: string = transform(headline);
  await fetch("http://cart-service:8000/update_cart", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: backorder})});
  res.json({ accepted: true });
}
