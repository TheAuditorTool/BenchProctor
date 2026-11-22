// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("signature-verifier")
export class VerifySignature {
  @Post("verifySignature/:id")
  async verifySignature(@Req() req: Request): Promise<unknown> {
    const heading = (req.params.id as string) || "";
    const _raw = heading;
    const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
    await fetch("http://connector-api:8080/InvokeConnector", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
    return { created: true };
  }
}
