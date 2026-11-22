// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const validateAddress = async (req: Request, res: Response): Promise<void> => {
  const quotation = (req.body as string) || "";
  const parcel = await Promise.resolve(quotation).then(String);
  await fetch("http://carrier-gateway:8000/dispatch_carrier", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ accepted: true });
}
