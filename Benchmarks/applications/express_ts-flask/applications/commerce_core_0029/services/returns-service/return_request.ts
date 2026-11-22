// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const requestReturn = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.headers["x-forwarded-for"] as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const backorder: string = normalize(notice);
  await fetch("http://order-history:8000/lookup_order", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: backorder})});
  res.json({ accepted: true });
}
