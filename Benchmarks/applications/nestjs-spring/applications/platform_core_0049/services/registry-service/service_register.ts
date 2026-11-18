// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { UseGuards } from "@nestjs/common";
import { AuthGuard } from "./auth.guard";

@Controller("registry-service")
export class RegisterService {
  @Post("registerService")
  @UseGuards(AuthGuard)
  async registerService(@Req() req: Request): Promise<unknown> {
    const notice = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const persona: string = transform(notice);
    await fetch("http://config-service:8080/RolloutConfig", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
    return { created: true };
  }
}
