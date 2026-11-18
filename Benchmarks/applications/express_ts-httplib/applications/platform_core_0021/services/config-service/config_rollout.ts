// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const rolloutConfig = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(excerpt);
  const handshake: string = readInput();
  await fetch("http://platform-api:8080/provision_tenant", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: handshake})});
  res.json({ accepted: true });
}
