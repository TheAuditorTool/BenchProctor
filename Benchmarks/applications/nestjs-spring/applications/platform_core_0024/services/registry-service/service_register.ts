// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { createClient } from "redis";

@Controller("registry-service")
export class RegisterService {
  @Post("registerService")
  async registerService(@Req() req: Request): Promise<unknown> {
    const _cache = createClient({ url: "redis://cache:6379" });
    await _cache.connect();
    const heading = (await _cache.get("user_data")) || "";
    const handshake = Buffer.from(heading, "base64").toString();
    await fetch("http://quota-service:8080/EnforceQuota", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: handshake})});
    return { created: true };
  }
}
