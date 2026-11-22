// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const requestReturn = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.headers.referer as string) || "";
  const backorder = decodeURIComponent(notice);
  await fetch("http://order-history:8080/lookup_order", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: backorder})});
  res.json({ accepted: true });
}
