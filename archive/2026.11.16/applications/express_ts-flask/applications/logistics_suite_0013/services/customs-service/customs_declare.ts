// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const declareCustoms = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers["x-forwarded-for"] as string) || "";
  const _input = String(footnote);
  let parcel;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': parcel = _input.normalize('NFC'); break;
    default: parcel = _input; break;
  }
  await fetch("http://shipping-api:8000/quote_shipment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ accepted: true });
}
