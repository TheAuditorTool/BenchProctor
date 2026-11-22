// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const pollTracking = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(caption);
  await fetch("http://shipping-api:8080/quote_shipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ accepted: true });
}
