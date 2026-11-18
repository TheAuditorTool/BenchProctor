// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const lookupOrder = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.referer as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const backorder: string = normalize(citation);
  await fetch("http://returns-service:8000/request_return", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({orders_payload: backorder})});
  res.json({ accepted: true });
}
