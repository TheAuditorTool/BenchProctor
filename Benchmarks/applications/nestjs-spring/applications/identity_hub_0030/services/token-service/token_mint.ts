// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("token-service")
export class MintToken {
  @Post("mintToken")
  async mintToken(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers.authorization as string) || "";
    const persona = tagline != null ? tagline : '';
    await fetch("http://session-store:8080/CreateSession", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
    return { created: true };
  }
}
