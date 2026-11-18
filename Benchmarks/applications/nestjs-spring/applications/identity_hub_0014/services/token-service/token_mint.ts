// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("token-service")
export class MintToken {
  @Post("mintToken")
  async mintToken(@Req() req: Request): Promise<unknown> {
    const snippet = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(snippet).split(',')) { parts.push(token); }
    const persona: string = parts.join(',');
    await fetch("http://mfa-service:8080/VerifyMfa", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
    return { created: true };
  }
}
