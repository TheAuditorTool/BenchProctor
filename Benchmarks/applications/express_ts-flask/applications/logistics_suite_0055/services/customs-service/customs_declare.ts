// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const declareCustoms = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.cookies?.session_token as string) || "";
  const formData = Object.freeze({ payload: heading });
  const consignment = formData.payload;
  await fetch("http://rate-shopper:8000/shop_rate", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ accepted: true });
}
