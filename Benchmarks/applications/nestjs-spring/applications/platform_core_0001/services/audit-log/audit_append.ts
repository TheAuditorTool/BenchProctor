// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("audit-log")
export class AppendAudit {
  @Post("appendAudit")
  async appendAudit(@Req() req: Request): Promise<unknown> {
    const tagline = (req.body as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const persona: string = normalize(tagline);
    await fetch("http://platform-api:8080/ProvisionTenant", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
    return { created: true };
  }
}
