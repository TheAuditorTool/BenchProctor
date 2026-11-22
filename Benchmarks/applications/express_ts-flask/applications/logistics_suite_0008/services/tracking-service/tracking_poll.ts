// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const pollTracking = async (req: Request, res: Response): Promise<void> => {
  const caption = ((req as any).files?.[0]?.originalname as string) || "";
  const consignment = String(caption).slice(0, 200);
  await fetch("http://shipping-api:8000/quote_shipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ accepted: true });
}
