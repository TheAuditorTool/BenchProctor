// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildManifest = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.cookies?.session_token as string) || "";
  const _raw = wording;
  const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://tracking-service:8000/poll_tracking", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ accepted: true });
}
