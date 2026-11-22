// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const dispatchCarrier = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.referer as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(citation);
  const parcel: string = readInput();
  await fetch("http://shipping-api:8080/quote_shipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ accepted: true });
}
