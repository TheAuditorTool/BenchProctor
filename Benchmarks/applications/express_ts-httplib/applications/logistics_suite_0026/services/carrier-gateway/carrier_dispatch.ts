// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const dispatchCarrier = async (req: Request, res: Response): Promise<void> => {
  const citation = (req.headers.referer as string) || "";
  const parcel = citation != null ? citation : '';
  await fetch("http://manifest-builder:8080/build_manifest", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ accepted: true });
}
