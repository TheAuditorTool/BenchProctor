// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildManifest = async (req: Request, res: Response): Promise<void> => {
  const wording = (req.params.id as string) || "";
  let consignment: string = '';
  const onInput = (v: string): void => { consignment = v; };
  onInput(wording);
  if (!req.session || !req.session.user) { res.status(401).json({error:"unauthorized"}); return; }
  await fetch("http://tracking-service:8080/poll_tracking", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: consignment})});
  res.json({ accepted: true });
}
