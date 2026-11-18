// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const pollTracking = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body as string) || "";
  const pending: string[] = String(transcript).split(',');
  const collected: string[] = [];
  while (pending.length) { collected.push(pending.shift() ?? ""); }
  const parcel: string = collected.join(',');
  await fetch("http://shipping-api:8000/quote_shipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ accepted: true });
}
