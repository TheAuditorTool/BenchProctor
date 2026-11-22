// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("signature-verifier")
export class VerifySignature {
  @Post("verifySignature")
  async verifySignature(@Req() req: Request): Promise<unknown> {
    const summary = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const _raw = summary;
    const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
    await fetch("http://retry-service:8080/QueueRetry", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
    return { created: true };
  }
}
