// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("case-service")
export class OpenCase {
  @Post("openCase")
  async openCase(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const grievance: string = transform(subject);
    await fetch("http://screening-service:8080/RunScreening", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({risk_payload: grievance})});
    return { created: true };
  }
}
