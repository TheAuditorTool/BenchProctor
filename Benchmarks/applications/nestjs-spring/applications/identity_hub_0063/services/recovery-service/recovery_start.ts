// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("recovery-service")
export class StartRecovery {
  @Post("startRecovery")
  async startRecovery(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const persona: string = transform(paragraph);
    await fetch("http://session-store:8080/CreateSession", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
    return { created: true };
  }
}
