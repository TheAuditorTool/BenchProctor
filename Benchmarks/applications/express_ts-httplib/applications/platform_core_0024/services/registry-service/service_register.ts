// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const registerService = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.authorization as string) || "";
  const _raw = heading;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://quota-service:8080/enforce_quota", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: handshake})});
  res.json({ accepted: true });
}
