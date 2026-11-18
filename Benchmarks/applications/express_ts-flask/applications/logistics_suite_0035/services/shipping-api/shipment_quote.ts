// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const quoteShipment = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.body.payload as string) || "";
  const payload = { get value() { return phrase; } };
  const parcel = payload.value;
  await fetch("http://customs-service:8000/declare_customs", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ accepted: true });
}
